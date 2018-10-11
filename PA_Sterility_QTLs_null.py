# Power analysis calculator for QTL detection strength
# Null simulation assumes no two locus incompatibility, determines the greatest p-value across genome by chance

# Takes input files from SIBSAM (Genetic Mapping by Bulk Segregant Analysis in Drosophila: Experimental Design and Simulation-Based Inference
# John E. Pool Genetics Early online September 21, 2016; https://doi.org/10.1534/genetics.116.192484) 


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
	# generate various lists
	sterile_focal_counts = []
	sterile_nonfocal_counts = []
	fertile_focal_counts = []
	fertile_nonfocal_counts = []
	combined_list_sterile = []
	combined_list_fertile =[]
	
	# read in file
	reader = csv.reader(File, dialect='tab_delim')
	#Range r value corresponds to (3/16)*500 sterile + 3/16*(250) sterile replicates
	#Range calue r2 corresponds to 500 fertile replicates
	r = list(range(0, 367))
	r2 = list(range(367, 2000))
	
	# Generate tuples of all pairwise window values and add to master list
	for row_number, row in read_lines(reader, r):
		row_tuples = list(it.combinations(row, 2))
		combined_list_sterile.append(row_tuples)
	# Rearrange list of tuples such that windows are grouped in lists, not rows
	
	window_list_sterile = map(list, zip(*combined_list_sterile))
	# calculate proportion of sterile focal and non-focal for each window

	# output for this loop produces two new lists of focal/non-focal counts by window
	for window in window_list_sterile:
		sterile_focal = []
		sterile_nonfocal =[]
		for pair in window:
			if pair==('0', '2'):
				sterile_focal.append(1)
			else:
				sterile_nonfocal.append(1)
	# Sum focal/nonfocal values per row in list for single value per window
		sumsf = sum(sterile_focal)
		sumnsf = sum(sterile_nonfocal)
		sterile_focal_counts.append(sumsf)
		sterile_nonfocal_counts.append(sumnsf)

	
	# Reset reader iterator
	File.seek(0)
	# repeat similar iteration for fertile simulated replicates	
	for row_number, row in read_lines(reader, r2):
			row_tuples2 = list(it.combinations(row, 2))
			combined_list_fertile.append(row_tuples2)


	window_list_fertile = map(list, zip(*combined_list_fertile))

	for window in window_list_fertile:
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

File.close()

# combine focal and non-focal sums
sterile_tuples = map(list, zip(sterile_focal_counts, sterile_nonfocal_counts))
fertile_tuples = map(list, zip(fertile_focal_counts, fertile_nonfocal_counts))


# make 2x2 matrices for each window
fisher_groups = map(list, zip(sterile_tuples, fertile_tuples))

p_values = []

# calculate Fisher's Exact for each window and obtain p-values
for groups in fisher_groups:
	oddsratio, pvalue = sp.fisher_exact(groups)
	p_values.append(pvalue)

# Determine the lowest window p-value and print it
lowest_pvalue = min(p_values)
print(lowest_pvalue)
