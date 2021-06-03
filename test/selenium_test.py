#! /usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

"""
This is just a test script to test out the web interface for the Bullhorn Search app.
"""
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
browser = webdriver.Chrome(options=options)
# Get the main page
browser.get("http://192.168.1.103")