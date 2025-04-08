# main.py
# https://disease.sh/docs/#/

from getAPIPackage.getAPI import*
from printPackage.print import*
from CSVPackage.CSV import *

if __name__ == "__main__":

    api = Api()
    parsed_json = api.get_api_data("https://disease.sh/v3/covid-19/states/Ohio")
