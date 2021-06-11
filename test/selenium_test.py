#! /usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

creds = []
with open("creds/auth_creds.txt", "r") as f:
    creds = f.readlines()
client_id = creds[0][:(len(creds[0])-1)]
client_secret = creds[1][:(len(creds[1])-1)]
username = creds[2][:(len(creds[2])-1)]
password = creds[3][:(len(creds[3])-1)]
"""
This is just a test script to test out the web interface for the Bullhorn Search app.
"""
# Using Google Chrome webdriver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

# using firefox for the browser
#profile = webdriver.FirefoxProfile()
#profile.set_preference("browser.privatebrowsing.autostart", True)
#options = webdriver.FirefoxOptions()
#options.set_headless()
#browser = webdriver.Firefox(firefox_profile=profile, options=options)
# Get the main page
browser.get("http://localhost:800")
time.sleep(7.0)
try:
    """
    - "WebDriverWait" => This is used to wait for the page to load for a piece
    of content to show up on the web page. I am using this because after the
    user logs in, the page takes some time to retrieve the data after logging
    in with their API credentials.
    - "By" => it is another way of locating elements with Selenium. To see the different
    applications of using "By", check out this documentation link below:
    Link: https://selenium-python.readthedocs.io/locating-elements.html
    - "ec" (short for expected_condition) -> the conditions to expect from the web page.
    """
    # check for the title
    main_title = WebDriverWait(browser, 20).until(
        ec.presence_of_element_located((By.CLASS_NAME, "Title"))
    )
    if "Bullhorn Candidate Date Added Search" not in main_title.text:
        raise 
except Exception as e:
    print("Could not load the web page. Please check your React code")
    browser.close()
# get to the login page
login = browser.find_element_by_link_text("Login")
login.click()
time.sleep(5.0)
try:
    login_title = browser.find_element_by_class_name("Title")
    login_subtitle = browser.find_element_by_class_name("Subtitle")
    login_div = browser.find_element_by_class_name("LoginDiv")
    form = browser.find_element_by_class_name("Login")
except Exception as e:
    print("Looks like the web page did not form properly.")
    browser.close()
try:
    input_client = browser.find_element_by_name("clientID")
    print("Found client ID")
    input_secret = browser.find_element_by_name("clientSecret")
    print("Found client secret")
    input_user = browser.find_element_by_name("username")
    print("Found the username")
    input_passwd = browser.find_element_by_name("password")
    print("Found the password")
    input_button = browser.find_element_by_id("submit-login")
    print("Found the button!")
except Exception as e:
    print("Looks like the form page did not render properly.")
    browser.close()
input_client.send_keys(client_id)
input_secret.send_keys(client_secret)
input_user.send_keys(username)
input_passwd.send_keys(password)
input_button.click()
try:
    token_content = WebDriverWait(browser, 60).until(
        ec.presence_of_element_located((By.CLASS_NAME, "Paragraph"))
    )
    time.sleep(5.0)
except Exception as e:
    print("Sorry, we could not get the loaded content from the page...")
    browser.close()
time.sleep(5.0)
search = browser.find_element_by_link_text("Search")
search.click()
time.sleep(6.0)
"""We are using the Select class to work with the drop down"""
search_drop_down = Select(browser.find_element_by_name("date-option"))

search_drop_down.select_by_value("Single")
time.sleep(1.0)
try:
    single_search = browser.find_element_by_id("single-search")
except Exception as e:
    print("The single date search did not render properly")
    browser.close()
search_drop_down.select_by_value("Between")
time.sleep(1.0)
try:
    between_search = browser.find_element_by_id("between-search")
except Exception as e:
    print("The between date search did not render properly")
    browser.close()
print("Hooray! The test finished without any issues!!")
print("Your app is good for deployment!")
browser.quit()
