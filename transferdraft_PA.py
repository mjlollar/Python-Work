# Power analysis calculator for QTL detection strength
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
	sterile_focal = []
	sterile_nonfocal = []
	reader = csv.reader(File, dialect='tab_delim')
	r = list(range(142))
	#Combine windows on each row into tuples of all pairwise window values
	for row_number, row in read_lines(reader, r):
		row_tuples = list(it.combinations(row, 2))
# need to add a function to combine all tuples from each position in a list so that I have 
# 141 new lists each with 500 tuple values
		for x,y in row_tuples:
			if not (x,y)==('0','2'):
				sterile_nonfocal.append(1)
			elif (x,y)==('0','2'):
				sterile_focal.append(1)
			else:
				pass
	sumsf = sum(sterile_focal)
	sumsnf = sum(sterile_nonfocal)
					
			



	
	pvalue = sp.fisher_exact([[sumsf,sumsnf], [sumff,sumfnf]]
