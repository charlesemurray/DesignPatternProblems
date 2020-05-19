#! /usr/bin/env python
# Question:
# Implement the ability to swap out different strategies in the following code.
# The strategies are as follows
# - In Memory Sort
# - Large Number of Records Sort
# - Large Size of Records Sort
#observer pattern
#Problems:
# - Making sure only one of the observers runs
# - Adding a new observer potentially requires changes to others
# Advantages
# - Clear view of what sorting methods we have
# - 

# wrong
# class CSV:
# 	def __init__(self, location):
# 		self.file = open(location, "r")
# 		self.sorting_methods = [InMemorySorting, LargeNumberRecordsSorting, LargeSizeRecordsSorting]
# 	def sort(self):
# 		for sorting_method in self.sorting_methods:
# 			sorting_method(self.file).sort()
# class SortingStrategy:
# 	def __init__(self, file):
# 		pass
# 	def sort():
# 		pass
# class InMemorySorting(SortingStrategy):
# 	def sort():
# 		pass
# class LargeNumberRecordsSorting(SortingStrategy):
# 	def sort():
# 		pass
# class LargeSizeRecordsSorting(SortingStrategy):
# 	def sort():
# 		pass

# Correct Observer Pattern
class CSV:
	def __init__(self):
		self.sorting_methods = []

	def attach(self, sort_method):
		self.sorting_method.append(sort_method)

	def detach(self, sort_method):
		self.sorting_method.remove(sort_method)

	def sort(location):
		for method in self.sorting_method:
			method.sort(location)

class LargeFile:

class SmallFile:

	def sort():
		if length < cutoff:


class SortingStrategy:
	def __init__(self, csv):
		csv.attach(self)
	def sort(location):
		pass
class InMemorySorting(SortingStrategy):
	def sort(location):
		pass
class LargeNumberRecordsSorting(SortingStrategy):
	def sort(location):
		pass
class LargeSizeRecordsSorting(SortingStrategy):
	def sort(location):
		pass

class CSVWrapper:
	def __init__(self):
		csv = CSV()
		large = LargeFile(csv)
		small = SmallFile(csv)
		InMemory(small)
		InMemory(csv)
		LargeNumberRecordSorting(csv)
		LargeSizeRecordSorting(csv)
		return csv

def main():
	csv = CSVWrapper()
	csv.sort("any file")
	csv.sort("Another file")
	csv = CSV()
	InMemory(csv)


# class SortingAgent:
# 	def __init__(self, file):
# 		self.file = file
# 		self.strategy_list = [InMemorySorting, LargeNumberRecordsSorting, LargeSizeRecordsSorting] 
# 	def get_strategy(self, cutoff_size_file, cutoff_size_record):
# 		file_size = os.stat(self.file).st_size 
# 		#calculate size of first few records of csv file
# 		with self.file as file:
# 			i = 0
# 			total_length = 0
# 			while i < 5:
# 				total_length += len(file.readline())
# 				i += 1
# 		first_5_records_average_length = total_length//5
# 		if column_size > self.cutoff_size_record:
# 			strategy = LargeSizeRecordsSorting(self.file).sort
# 		elif file_size > self.cutoff_size_file:
# 			strategy = LargeNumberRecordsSorting(self.file).sort
# 		else:
# 			strategy = InMemorySorting(self.file).sort
		
		
Client:file_location -> CSV -> LargeSizeRecordSorting
							-> LargeNumberRecordsSorting
							-> InMemorySorting





#attempted strategy pattern
import os
class CSV:
	def __init__(self, location):
		#get the handle of the CSV
		self.file = open(location, "r")
	def sort(self):
		#cut off for large size record sorting
		
		#get the whole size of csv file
		file_size = os.stat(self.file).st_size 
		#calculate size of first few records of csv file
		with self.file as file:
			i = 0
			total_length = 0
			while i < 5:
				total_length += len(file.readline())
				i += 1
		first_5_records_average_length = total_length//5
		SortingAgent.sorting(self.file)
		
class SortingAgent:
	def __init__(self, file, cutoff_size_file = default, cutoff_size_record = default):
		self.file = file
		self.cutoff_size_record = cutoff_size_file
		self.cutoff_size_file = cutoff_size_record
	def sorting(self, file_size, column_size):
		if column_size > self.cutoff_size_record:
			LargeSizeRecordsSorting(self.file).sort()
		elif file_size > self.cutoff_size_file:
			LargeNumberRecordsSorting(self.file).sort()
		else:
			InMemorySorting(self.file).sort()




class SortingStrategy:
	def __init__(self, file):
		pass
	def sort():
		pass
class InMemorySorting(SortingStrategy):
	def sort():
		pass
class LargeNumberRecordsSorting(SortingStrategy):
	def sort():
		pass
class LargeSizeRecordsSorting(SortingStrategy):
	def sort():
		pass


import os
class CSV:
	def __init__(self, location, strategy):
		#get the handle of the CSV
		self.file = open(location, "r")
		self.strategy = strategy
	def sort(self):
		self.strategy.sort()

		
class SortingAgent:
	__instance = None

	def __init__(self):
		if Singleton.__instance != None:
			raise "This is a singleton"
		else:
			self.cutoff_size_record = 20
			self.cutoff_size_file = 1000
			Singleton.__instance = self

	@classmethod
	def getInstance():
		if cls.__instance == None:
			cls()
		return cls.__instance

	def setLocation(self, location):
		self.location = location

	def determineStrategy(self, location)
		#get the whole size of csv file
		file_size = os.stat(location).st_size 
		#calculate size of first few records of csv file
		with open(location, "r") as file:
			i = 0
			total_length = 0
			while i < 5:
				total_length += len(file.readline())
				i += 1
		first_5_records_average_length = total_length//5
		if column_size > self.cutoff_size_record:
			strategy = LargeSizeRecordsSorting(self.file)
		elif file_size > self.cutoff_size_file:
			strategy = LargeNumberRecordsSorting(self.file)
		else:
			strategy = InMemorySorting(self.file)
		return CSV(location, strategy)

	def getCSV(self, location):
		self.determineStrategy(location)
		

def main():
	filename =
	csv = SortingAgent.getCSV(filename)
	csv.setLocation(file_name).sort()
	csv.sort()
	csv = SortingAgent.getCSV(another_file)
	csv.sort()




class SortingStrategy:
	def __init__(self, file):
		pass
	def sort():
		pass
class InMemorySorting(SortingStrategy):
	def sort():
		pass
class LargeNumberRecordsSorting(SortingStrategy):
	def sort():
		pass
class LargeSizeRecordsSorting(SortingStrategy):
	def sort():
		pass

"""
Sort CSV file by multiple columns, writing output to sorted CSV file.
Recommended for files saved in Windows CSV format.
Useful for situations where data file is too large for Excel.
: param source_file.csv : source csv file. Must end in .csv 
: param sort column 1 : first sort in Excel-like column number (i.e., 1 ... N)
                        Use negative number to indicate descending sort,
                        Positive number to indicate ascending sort_step
: param sort column N : next sort in Excel-like column number (i.e., 1 ... N)
Result is a sorted destination csv of name format input_file_sorted.csv.
EXAMPLES: 
	foo.csv has Column 1 = last_name, Column 2 = first_name
				Column 3 = dob, Column 4 = height
	Sort foo.csv by last_name then first_name then DOB:
		sortCSV.py foo.csv 1 2 3
	Sort the same but sort DOB descending (vs ascending):
		sortCSV.py foo.csv 1 2 -3
	Sort foo.csv by last_name then first_name then height, tallest to short:
		sortCSV.py foo.csv 1 2 -4
	Output written to foo_sorted.csv
Move to /usr/local/bin and chmod +x to use as command.
Can easily convert to function for real-time application.
"""

import sys
import csv
from sys import argv
from operator import itemgetter

num_arguments = len(argv)

# Check usage and provide help
if num_arguments == 2 and argv[1] in ('-h', '-help'):
	print "Usage: %s input_file.csv 1st_sort_col ... nth_sort_col" % argv[0]
	print "Example: %s foo.csv 1 2 -9" % argv[0]
	print "\tSorts foo.csv on 1st and 2nd columns (ascending) then 9th descending."
	sys.exit()
elif num_arguments < 3: # Guidance on arguments to pass
	usage = "Usage: %s input_file.csv 1st_sort_col ... nth_sort_col" % argv[0]
	error = "You passed only %d arguments" % num_arguments
	sys.exit("%s -- %s" % (usage, error))
if '.csv' not in argv[1]: # Ensure using a CSV file
	usage = "Usage: %s input_file.csv 1st_sort_col ... nth_sort_col" % argv[0]
	error = "You passed %r for input_file.csv" % argv[1]
	sys.exit("%s -- %s" % (usage, error))

# Create the output file as input with _sorted before .csv extension
input_file = argv[1]
output_file = input_file.replace('.csv', '_sorted.csv')

# Ensure you can open the source and target files
try:
	source = open(input_file, 'r')
except:
	e = sys.exc_info()[0]
	sys.exit("Error - Could not open input file %r: %s" % (input_file, e))
try: 
	target = open(output_file, 'w')
except:
	e = sys.exc_info()[0]
	sys.exit("Error - Could not open output file %r: %s" % (output_file, e))
print "\nSorting data from %r into %r, inside out" % (input_file, output_file)

# Now create a list of sorting tuples where the first item is the index of 
# the data object you wish to sort and the second item is the type of sort,
# Ascending (Reverse is False) or Descending (Reverse is True)
sorts = []
for i in range (2, num_arguments): # Skip script name and input filename
	# Ensure you are passed Excel-like column numbers
	try: 
		sort_arg = int(argv[i])
	except:
		e = sys.exc_info()[0]
		sys.exit("Error - Sort column %r not an integer: %s." % (argv[i], e))
	if sort_arg == 0:
		sys.exit("Error - Use Excel-like column numbers from 1 to N")
	# Create a tuple for each as described above
	if sort_arg > 0:
		sorts.append((sort_arg - 1, False)) # Convert column num to index num
	else:
		sorts.append(((-1 * sort_arg) - 1, True))

# Read in the data creating a label list and list of one tuple per row
reader = csv.reader(source)
row_count = 0 
data=[] 
for row in reader:
	row_count += 1
	# Place the first row into the header
	if row_count == 1:
		header = row
		continue
	# Append all non-header rows into a list of data as a tuple of cells
	data.append(tuple(row))

# Sort is stable as of Python 2.2. As such, we can break down the 
# complex sort into a series of simpler sorts. We just need to remember 
# to REVERSE the order of the sorts.
for sort_step in reversed(sorts):
	print 'Sorting Column %d ("%s") Descending=%s' % \
	(sort_step[0] + 1, header[sort_step[0]], sort_step[1]) # +1 for Excel col num
	data = sorted(data, key=itemgetter(sort_step[0]), reverse=sort_step[1])
print 'Done sorting %d data rows (excluding header row) from %r' % \
((row_count - 1), input_file)


# Now write all of this out to the new file
writer = csv.writer(target)
writer.writerow(header) # Write the header in CSV format
for sorted_row in data: # Wrtie the sorted data, converting to CSV format
	writer.writerow(sorted_row)
print 'Done writing %d rows (sorted data plus header) to %r\n' % \
(row_count, output_file) 

# Be good and close the files
source.closed
target.closed