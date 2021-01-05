"""
Task: Inheritance

Task 1: 

Complete the class "FileReader" so that when calling the lines() method the file is accessed line by line. The lines() method should then return a list of the lines file. 

Task 2: 

Create the class "CsvReader", so that the "File Reader" is extended to read a .csv-file instead. It should return a multidimensional list.

Important: Leave the reading of the file to the "FileReader", and extend the lines() - method in the CSV-Reader by the functionality, which is needed so that the multidimensional list is returned!
"""

class FileReader():
	def __init__(self, filename): #start with a constructor
		self.filename = filename

	def lines(self): #assign self as the parameter
		lines = []
		with open(self.filename, "r") as file: #open file
			for line in file: #go through every line
				lines.append(line.strip()) #append line and clean it up
		return lines #return line

class CsvReader(FileReader):
	def __init__(self, filename):
		super().__init__(filename)

		def lines(self):
			lines = super().lines()

			return[line.split(",") for line in lines]

"""			split_lines = []
			for line in lines:
				split_lines.append(line.split(","))
			return split_lines
"""
f = FileReader("./file.csv")
print(f.lines())

# Expected output:
# [surname, first_name, Doe, John, Miller, Monica]

f = CsvReader("./file.csv")
print(f.lines())
