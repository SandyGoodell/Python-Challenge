import os
import csv

# Path to retrieve data from the Resources file
budget_data_path = os.path.join('Resources','budget_data.csv')

# Read in the csv data
with open(budget_data_path,'r') as budget_data_file:
    #Split data on commas - using csv reader function - csv.reader()
    budget_data_reader = csv.reader(budget_data_file, ',')

    #Skip header
    next(budget_data_reader)
    