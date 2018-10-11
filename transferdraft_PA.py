# Power analysis calculator for QTL detection strength
# Null simulation assumes no two locus incompatibility, determines the greatest p-value across genome by chance
# test simulates one X-autosome incompatibility and one autosome-autosome incompatibility

import sys
import csv
import scipy.stats as sp
import itertools as it

csv.register_dialect('tab_delim', delimiter="\t", quoting=csv.QUOTE_NONE)

file_name = input("Insert replicate file:\n")

# function needed to read in rows as lines for list of tuple generation
def read_lines(csv_reader, row_list):
	for row_number, row in enumerate(csv_reader):
		if row_number in row_list:
			yield row_number, row

with open(file_name, 'r') as File:
	# generate all open lists that will be appended
	sterile_focal_counts = []
	sterile_nonfocal_counts = []
	fertile_focal_counts = []
	fertile_nonfocal_counts = []
	combined_list = []
	combined_list2 =[]
	
	# read in file
	reader = csv.reader(File, dialect='tab_delim')
	#Range value corresponds to (3/16)*500 sterile + 3/16*(250) sterile 
	r = list(range(0, 142))
	r2 = list(range(142, 501))
	
	# Combine windows on each row into tuples of all pairwise window values and add to master list
	for row_number, row in read_lines(reader, r):
		row_tuples = list(it.combinations(row, 2))
		combined_list.append(row_tuples)
	# Rearrange list of tuples such that windows are grouped in lists, not rows
	
	window_list = map(list, zip(*combined_list))
	# caclulate proportion of sterile focal and non-focal for each window
	
	# output for this loop produces two new lists of focal/non-focal counts by window
	for window in window_list:
		sterile_focal = []
		sterile_nonfocal =[]
		for pair in window:
			if pair==('0', '2'):
				sterile_focal.append(1)
			else:
				sterile_nonfocal.append(1)
	# Sum focal/nonfocal values per row in list for single value per widdow
		sumsf = sum(sterile_focal)
		sumnsf = sum(sterile_nonfocal)
		sterile_focal_counts.append(sumsf)
		sterile_nonfocal_counts.append(sumnsf)

	# Combine focal, nonfocal lists 
	sterile_tuples = map(list, zip(sterile_focal_counts, sterile_nonfocal_counts))

	r2 = list(range(142, 501))

	for row_number, row in read_lines(reader, r2):
		row_tuples = list
		


					
			



	
	pvalue = sp.fisher_exact([[sumsf,sumsnf], [sumff,sumfnf]]
