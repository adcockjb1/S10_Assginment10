# main.py
# https://disease.sh/docs/#/

from getAPIPackage.getAPI import*
from printPackage.print import*
from CSVPackage.CSV import *

if __name__ == "__main__":

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
