"""
Exercise!

Find out how often the name "Max" was given as a male first name in California between 1950 and 2000 (both inclusive)! Use the provided .csv file (.../data/names.csv)!
"""

"""n = "1975"
print(int(n) < 1990)

years = ["Year", "1990", "1992"]

for year in years:
	if year == "Year":
		continue
	print(int(year))"""

"""name = "Max"
gender = "M"
state = "CA"

with open("../content/data/names.csv", "r") as file:
	counter = 0
	for line in file:
		counter = counter + 1
		line_split = line.strip().split(",")
		if line_split[1] == name and line_split[3] == gender and line_split[4] == state:
			for line_split in file:
				if int(line_split[2]) <= 1990 and int(line_split[2]) >= 2000:
					print(line_split)
			print(line_split)"""

occurrences = 0 # creating viable to count occurrences of max

with open("../content/data/names.csv", "r") as file: # reading the names.csv using the with construct
	for line in file: # creating line with a for loop
		splitted = line.strip().split(",") # stripping line and splitting at the comma -- storing result as the variable splitted
		if splitted[2] == "Year": # if the 3rd value in the csv is Year then continue
			continue
		year = int(splitted[2]) # declaring the year variable from splitted as the 3rd value from the csv and storing as an integer
		
		if splitted[1] == "Max" and year >= 1950 and year <= 2000 and splitted[3] == "M" and splitted[4] == "CA": # filtering on name from the 2nd position, filter year between specified years, 
			occurrences = occurrences + int(splitted[5])

print(occurrences)