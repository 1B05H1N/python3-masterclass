"""
Introducing another module: CSV

In this lesson you will learn how to: 

Use the Python Module index (https://docs.python.org/3/py-modindex.html)
With modules even more comfortable.csv files with the example of the CSV.
"""

# go to https://docs.python.org/3/py-modindex.html, change version and check out modules

# find out version

import sys
print(sys.version)

# modules were made to make our lives easier

import csv
# check out how to use the module via https://docs.python.org/3/library/csv.html#module-csv
with open('fromnumbers.csv', newline='') as file:
    csv_file = csv.reader(file, delimiter=';', quotechar='"')
    for line in csv_file:
        print(line)

with open('fromexcel.csv', newline='') as file:
    csv_file = csv.reader(file, delimiter=';', quotechar='"')
    for line in csv_file:
        print(line)