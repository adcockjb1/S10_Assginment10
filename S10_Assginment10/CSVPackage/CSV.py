# CSV.py
# https://community.lambdatest.com/t/how-to-write-a-python-dictionary-to-csv-with-keys-as-headers/34274

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
