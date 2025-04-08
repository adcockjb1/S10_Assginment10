# print.py

# File Name : print.py
# Student Name: Asfia Siddiqui
# email: siddiqaf@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/10/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to execute an API call using a URL.

# Brief Description of what this module does:
# Citations: 

# Anything else that's relevant:


class PrintResult():
    def print_result(self, total_case, total_death, case_today, death_today, state):
        """
        Print descriptive statements
        @param total_case int: The total number of case of COVID-19
        @param total_death int: The total number of death due to COVID-19
        @param case_today int: The number of today's case of COVID-19
        @param death_today int: The number of today's death due to COVID-19
        @param state String: State 
        return descriptive statements
        """
        
        print("The total number of case of COVID-19 is " + str(total_case) + " in " + state)
        print("The total number of death due to COVID-19 is " + str(total_death) + " in " + state)
        print("The number of today's case of COVID-19 is " + str(case_today) + " in " + state)
        print("The number of today's death due to COVID-19 is " + str(death_today) + " in " + state)


