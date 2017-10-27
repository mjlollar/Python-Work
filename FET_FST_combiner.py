#!/usr/bin/env python3

import sys
import csv

csv.register_dialect('Comma_Delin', delimiter=',', quoting=csv.QUOTE_NONE)

#This is designed to work with output files of "LD_between_loci_filter_strongest_*.pl" files.

file_name1 = input("Insert LD FET file name:\n")

with open(file_name1, 'r') as File1:
	reader = csv.reader(File1, dialect='Comma_Delin')
	dict_FET = {}
	for rows in reader:
		try:
			key = (int(rows[1]), int(rows[0]))
			dict_FET[key] = rows[3]	
		except ValueError:
			for key in rows:
				del key
			continue
			
print("FET values for" + " " + str(file_name1) + " " + "compiled.")
	
#This is designed to work with output files of "FST_*_Chr*.pl".

file_name2 = input("Insert FST file name:\n")

with open(file_name2, 'r') as File2:
	reader = csv.reader(File2, dialect='Comma_Delin')
	dict_FST = {}
	for rows in reader:
		try:
			row1 = int(rows[1])
			row2 = int(rows[2])
			key = range(row1, row2)
			dict_FST[key] = rows[4]
		except ValueError:
				for key in rows:
					del[key]
				continue
				
print("FST values and SNP positions for" + " " + str(file_name2) + " " + "compiled")

dict_combined = {}

for key, value1 in dict_FET.items():
    dict_combined.setdefault(key, [value1]).extend(
        value2 for interval, value2 in dict_FST.items() if key[0] in interval)

new_file = input("Insert a file name for your new file, include .csv:\n")

with open(new_file, 'w', newline='') as File3:
	writer = csv.writer(File3, dialect='Comma_Delin', escapechar=' ')
	writer.writerow(["Fife Pos", "SNP Pos", "FETP", "FST"])
	writer.writerows([row[0]] + row[1] for row in dict_combined.items())

print(str(new_file) + ' ' + "has been created in your current directory.")
