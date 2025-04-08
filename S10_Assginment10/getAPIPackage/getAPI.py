# getAPI.py

# File Name : getAPI.py
# Student Name: Joseph Adcock
# email: adcockjb@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/10/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to execute an API call using a URL.

# Brief Description of what this module does:
# Citations: 

# Anything else that's relevant:


import json
import requests

class Api:

    def get_api_data(self, URL):
        """
        Receive API data and read it as dictionary format
        @param URL String: The URL of API
        @return data in dictionary format
        """
        response = requests.get(URL)
        json_string = response.content

        parsed_json = json.loads(json_string) # Now we have a python dictionary

        return parsed_json