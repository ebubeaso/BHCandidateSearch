#! /usr/bin/env python
import requests
import os
from getpass import getpass
"""
This simple Python script is used to get the Jenkins crumb issuer to run jobs from
the command line
"""
the_token = os.getenv('BH_TEST_TOKEN')
url = input("Enter the IP address of your Jenkins server: ")
username = os.getenv('BH_TEST_USER')
password = os.getenv('BH_TEST_PASS')
print("")
try:
    # This will try and fetch the crub data
    crumb = requests.get(f'http://{url}:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)',
    auth=(username, password), headers={'Content-Type': 'application/json'})
    if crumb.status_code == 200:
        result = crumb.text
        # this uses the index method to find the colon on the crumb response
        """
        The response of the Jenkins crumb starts with 'Jenkins-Crumb:' with the
        crumb code afterwards, so I used the index
        """
        crumb_code = result[(result.index(":")+1):]
        data = requests.get(f"http://{url}:8080/job/Bullhorn%20Candidate%20Search/build?token={the_token}",
            auth=(username,password), headers={'Content-Type': 'application/json',
            'Jenkins-Crumb': crumb_code})
        # check the status code of the execution
        if data.status_code == 201 or data.status_code == 200:
            print("Triggered Jenkins job")
        else:
            ("Triggering the SSH Shadowblaze job failed")
    else:
        print("Could not get the Jenkins crumb")
        raise
except Exception as e:
    #exception block to run if this job fails
    print("ERROR: Could not get the crumb info")
    print(str(e))