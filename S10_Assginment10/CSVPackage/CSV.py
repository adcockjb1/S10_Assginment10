# CSV.py

# File Name : CSV.py
# Student Name: Nogaye Gueye
# email: gueyene@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/10/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to execute an API call using a URL.

# Brief Description of what this module does: This module converts a Python dictionary into a CSV file and saves it to the specified filename.
# Citations: https://community.lambdatest.com/t/how-to-write-a-python-dictionary-to-csv-with-keys-as-headers/34274

# Anything else that's relevant:

import csv

class ConvertToCSV:
    def save_as_csv(self, filename, data):
        """
        Convert dictionary to CSV
        @param filename String: The desired file name(.csv)
        @param data dict: The dictionary of data
        @return CSV file
        """

        with open(filename, 'w', newline = '') as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)
