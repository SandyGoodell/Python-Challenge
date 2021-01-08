# imports (files)
import os
import csv

# import data (path)
file_to_open = os.path.join()

# declare global variables

# if using functions create 

# start loop - with open
with open(file_to_open, "r") as csvfile:
    csvreader = csv.reader(csvfile)

    # This skips the first row of the CSV file.
    next(csvreader)

    for row in csvreader:
        # do stuff with rows...

