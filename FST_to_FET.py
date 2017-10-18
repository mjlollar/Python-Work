#!/usr/bin/env python3

import sys
import csv

file_name1 = input("Insert LD FET file name:\n")

csv.register_dialect('Comma_Delin', delimiter=',', quoting=csv.QUOTE_NONE)

# Pulls SNP position and corresponding Fisher's Exact p-value and creates dictionary of values
with open(file_name1, 'r') as File1:
	reader = csv.reader(File1, dialect='Comma_Delin')
	dict1 = {}
	for rows in reader:
		key = rows[0]
		dict1[key] = rows[3]	
	del dict1['Pos1']
	print("Fife position and FET value for" + " " + str(file_name1) +" " + "compiled")		

 
file_name2 = input("Insert FST file name:\n")

#Pulls location and associated FST value and creates dictionary
with open(file_name2, 'r') as File2:
  reader = csv.reader(File2, dialect='Comma_Delin')
  dict2 = {} 
  for rows in reader:
      key = rows[0]
      dict2[key] = rows[2]
  del dict2['RGSite Cov']
  print("FST values for sites compiled")

#Next step is to compare key values between two dictionaries and combine values
#After comparison, output dictionary to new CSV

#Add exception?
