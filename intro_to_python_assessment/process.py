"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""
import tui
from intro_to_python_assessment import main
import csv

file = "covid_19_data.csv"

from collections import defaultdict

# TODO: Your code here
#- Retrieve a record with the serial number as specified by the user.
def retrieve_by_serialn(the_record):
    # Task: 15
    tui.serial_number()
    retrievable_number = int(input())
    # retrieving the user's input
    with open(the_record) as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        # for testing
       # print(rows[retrievable_number])
        return rows[retrievable_number]


###########################################################################
def retrieving_by_obs(the_record):
    results = []
    results2 = []
    # prompting the user to input a date
    tui.observation_dates()
    retrievable_date = input()
    # populating a list from the csv file
    with open(the_record, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',', quotechar='"')
        headings = next(csv_reader)
        for line in file:#.readlines():
            results = line.strip().split(',')
            results.append((results))
           # print(results)
    # extracting the needed results from that list.
            if retrievable_date in results:
                results2.append(results)
                # this line gets rid of the piramid
                results2 = line.strip().split(',')
                print(results2)
    #return results2 only shows one row



def retrieve_by_cr(the_record):
    d = {}
    for row in the_record:
        if row[3] not in d:
            d[row[3]] = []
        d[row[3]].append(row[1:])

    for x, y in d.items():
        print(x, y)



def summary(the_record):
    summary = {}

    with open(the_record, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',', quotechar='"')
        headings = next(csv_reader)
        for line in file.readlines():
            results = line.strip().split(',')

            if not results[3] in summary:
                summary[results[3]] = [0, 0, 0]
            cases = int(results[5])
            deaths = int(results[6])
            rec = int(results[7])
            summary[results[3]][0] += cases
            summary[results[3]][1] += deaths
            summary[results[3]][2] += rec

    return summary