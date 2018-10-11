 Power analysis calculator for QTL detection strength
# Null simulation assumes no two locus incompatibility, determines the greatest p-value across genome by chance
# test simulates one X-autosome incompatibility and one autosome-autosome incompatibility

import sys
import csv
import scipy.stats as sp
import itertools as it

csv.register_dialect('tab_delim', delimiter="\t", quoting=csv.QUOTE_NONE)

file_name = input("Insert replicate file:\n")

def read_lines(csv_reader, row_list):
	for row_number, row in enumerate(csv_reader):
		if row_number in row_list:
			yield row_number, row

with open(file_name, 'r') as File:
	reader = csv.reader(File, dialect='tab_delim')
	r = list(range(4))
	r2 = list(range(4, 7))
	combined_list = []
	combined_list2 = []
	sterile_focal_counts = []
	sterile_nonfocal_counts = []
	fertile_focal_counts = []
	fertile_nonfocal_counts = []
	
	for row_number, row in read_lines(reader, r):
		row_tuples = list(it.combinations(row, 2))
		combined_list.append(row_tuples)

	window_list =  map(list, zip(*combined_list))

	for window in window_list:
		sterile_focal = []
		sterile_nonfocal =[]
		for pair in window:
			if pair==('0', '2'):
				sterile_focal.append(1)
			else:
				sterile_nonfocal.append(1)
		
		sumsf = sum(sterile_focal)
		sumnsf = sum(sterile_nonfocal)
		sterile_focal_counts.append(sumsf)
		sterile_nonfocal_counts.append(sumnsf)

	sterile_tuples = map(list, zip(sterile_focal_counts, sterile_nonfocal_counts))
	
	for row_number, row in read_lines(reader, r2):
		row_tuples2 = list(it.combinations(row, 2))
		combined_list2.append(row_tuples2)

	print(combined_list2)

	window_list2 = map(list, zip(*combined_list2))


	for window in window_list2:
		fertile_focal =[]
		fertile_nonfocal = []
		for pair in window:
			if pair==('0', '2'):
				fertile_focal.append(1)
			else:
				fertile_nonfocal.append(1)

		sumff = sum(fertile_focal)
		sumfnf = sum(fertile_nonfocal)
		fertile_focal_counts.append(sumff)
		fertile_nonfocal_counts.append(sumfnf)

	fertile_tuples = map(list, zip(fertile_focal_counts, fertile_nonfocal_counts))







print("running")
