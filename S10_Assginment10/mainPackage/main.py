# main.py

# File Name : # main.py
# Student Name: Asfia Siddiqui
#               Nogaye Gueye
#               Joseph Adcock
#               Kengo Ishizuka
# email: siddiqaf@mail.uc.edu
#        gueyene@mail.uc.edu
#        adcockjb@mail.uc.edu
#        ishizuko@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/10/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to execute an API call using a URL.

# Brief Description of what this module does: This module serves as the entry point for the program.
# Citations: 

# Anything else that's relevant: https://disease.sh/docs/#/

from getAPIPackage.getAPI import*
from printPackage.print import*
from CSVPackage.CSV import *

if __name__ == "__main__":

    # Receive API data and read it as dictionary format
    api = Api()
    parsed_json = api.get_api_data("https://disease.sh/v3/covid-19/states/Ohio")

    #  Extract the data of total_case, total_death, case_today, death_today, and state from JSON
    total_case = parsed_json["cases"]
    total_death = parsed_json["deaths"]
    case_today = parsed_json["todayCases"]
    death_today = parsed_json["todayDeaths"]
    state = parsed_json["state"]

    # Print data
    prt = PrintResult()
    prt.print_result(total_case, total_death, case_today, death_today, state)

    # Convert to CSV
    csv = ConvertToCSV()
    filename = 'data.csv'
    csv.save_as_csv(filename, parsed_json)
