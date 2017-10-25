#!/usr/bin/env python3

import sys
import csv

file_name1 = input("Insert LD FET file name:\n")

csv.register_dialect('Comma_Delin', delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')

#This will only work with SNP_LD_file_DOR0.001 files. Other files may contain columns in different orders.
#Pulls Site position with corresponding FET value

with open(file_name1, 'r') as File1:
	reader = csv.reader(File1, dialect='Comma_Delin')
	dict_FET = {}
	for rows in reader:
		key = rows[0]
		dict_FET[key] = rows[3]	
	del dict_FET['Pos1']
	print("Fife position and FET value for" + " " + str(file_name1) + " " + "compiled")		
	File1.close()
	
print(dict_FET)
	
file_name2 = input("Insert FST file name:\n")

#This will only work for FST_sites output files.  Other files may contain columns in different orders.
#Pulls Site position with corresponding FST value 

with open(file_name2, 'r') as File2:
	reader = csv.reader(File2, dialect='Comma_Delin')
	dict_FST = {}
	for rows in reader:
		key = rows[1]
		dict_FST[key] = rows[2]
	del dict_FST['Position']
	File2.close()
	
print("FST values and SNP positions for" + " " + str(file_name2) + " " + "compiled")

print(dict_FST)

#Match site values and combine FET and FST values, None where value is not present
		
keys = dict_FET.keys()
dict_combined = {k: [dict_FET.get(k), dict_FST.get(k)] for k in keys}		


print("--------------------------------------------")
print(dict_combined)


new_file = input("Insert a file name for your new file, include .csv:\n")

#Write combined values to a new file

with open(new_file, 'w', newline='') as File3:
	writer = csv.writer(File3, dialect='Comma_Delin')
	writer.writerows([row[0]] + row[1] for row in dict_combined.items())

print(str(new_file) + ' ' + "has been created in your current directory!")
	
