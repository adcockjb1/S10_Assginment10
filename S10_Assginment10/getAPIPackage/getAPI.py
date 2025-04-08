# getAPI.py

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