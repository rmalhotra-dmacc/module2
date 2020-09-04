"""""
Program: camper_age_input.py
Author: Rajiv Malhotra
Last Modified Date: 09/03/2020
 
The program will prompt for the age of camper who is attending camp 
and convert the age in years to months via a function call then print the result.
"""""
import constants

def convert_to_months(years):
    months = years * constants.MONTHS
    return months


if __name__ == '__main__':
    age_in_years = input("Enter age of camper: ")
    age_in_months = convert_to_months(int(age_in_years))
    print("{} years is {} months".format(age_in_years, age_in_months))
