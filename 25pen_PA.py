# Power Analysis for the detection of Sterility QTLs
# Model assumes two unique two-locus recessive sterility loci. One non-focal X-Autosome locus and one focal Autosome-Autosome locus
# Model also assumes 25% penetrance of sterile loci.
# Allows you to input the number of flies you wish to sequence, plus those used to scan, adding in additional steriles for sequencing
# Inputs include generated samples from SIBSAM (Pool 2015) and number of flies to be seuqenced/phenotypically scanned
# Input should be in the format: python3 25pen_PA.py "Ancestry file.txt" # of sequenced +1" "# of screened + # sequenced + 1"
# Example input for 200 sequenced flies and 1200 scanned flies: python3 25pen_PA.py F2MaleAnc2000_1.txt 201 1401 

import sys
import csv
import scipy.stats as sp
import itertools as it
import random as ran

csv.register_dialect('tab_delim', delimiter="\t", quoting=csv.QUOTE_NONE)

file_name = sys.argv[1]
range_value1 = int(sys.argv[2])
range_value2 = int(sys.argv[3])

# Function to enumerate replicates in ancestry file

def read_lines(csv_reader, row_list):
	for row_number, row in enumerate(csv_reader):
		if row_number in row_list:
			yield row_number, row

with open(file_name, 'r') as File:
	replicate_list = []
	replicate_list_scan = []
	reader = csv.reader(File, dialect='tab_delim')
	window1 = list(range(0, range_value1))
	window2 = list(range(range_value1, range_value2))

	# Generate all pairwise combinations of window pairs

	for row_number, row in read_lines(reader, window1):
		row_tuples = list(it.combinations(row, 2))
		replicate_list.append(row_tuples)

	# Randomly picked X-A and A-A pair that are defined as our sterility loci
	
	window_list = list(map(list, zip(*replicate_list)))
	window_sterileXA = window_list[25000]
	counted_window_sterile_XA = list(enumerate(window_sterileXA))
	window_sterileAA = window_list[79800]
	counted_window_sterile_AA = list(enumerate(window_sterileAA))
	
	sterile_count_AA = []
	fertile_count_AA = []
	fertile_focal_count_AA = []

	# Count sterile A-A numbers in sequenced and fertile focal non-penatrent

	for window in counted_window_sterile_AA:
		if window[1] == ('0', '2'):
			prob = ran.randint(0, 3)
			if prob == 1:
				sterile_count_AA.append(window[0])
			else:
				fertile_focal_count_AA.append(window[0])
		else:
			fertile_count_AA.append(window[0])	
	
	sterile_count_XA = []
	fertile_count_XA = []

	# Count sterile X-A numbers in sequenced

	for window in counted_window_sterile_XA:
		if window[1] == ('0', '2'):
			prob = ran.randint(0, 3)
			if prob ==1:
				sterile_count_XA.append(window[0])
			else:
				fertile_count_XA.append(window[0])
		else:
			fertile_count_XA.append(window[0])

	# Reset file iterator
	
	File.seek(0)

	# Repeat process of combinations for scanned group

	for row_number, row, in read_lines(reader, window2):
		row_tuples2 = list(it.combinations(row, 2))
		replicate_list_scan.append(row_tuples2)

	window_list2 = list(map(list, zip(*replicate_list_scan)))
	window_sterileXA_scan = window_list2[25000]
	counted_window_sterile_XA_scan = list(enumerate(window_sterileXA_scan, range_value1))
	window_sterileAA_scan = window_list2[79800]
	counted_window_sterile_AA_scan = list(enumerate(window_sterileAA_scan, range_value1))

	sterile_count_AA_scan = []

	for window in counted_window_sterile_AA_scan:
		if window[1] == ('0', '2'):
			prob = ran.randint(0, 3)
			if prob == 1:
				sterile_count_AA_scan.append(window[0])
			else:
				pass
		else:
			pass
			
	sterile_count_XA_scan = []

	for window in counted_window_sterile_XA_scan:
		if window[1] == ('0', '2'):
			prob = ran.randint(0, 3)
			if prob == 1:
				sterile_count_XA_scan.append(window[0])
			else:
				pass
		else:
			pass
	
	combined_sterile_AA = sterile_count_AA + sterile_count_AA_scan

	combined_sterile_XA = sterile_count_XA + sterile_count_XA_scan
	
	int_sterile_XA_set = set(combined_sterile_XA)
	int_sterile_AA_set = set(combined_sterile_AA)
	
	final_sterile_XA_list = list(int_sterile_XA_set - int_sterile_AA_set)
	
	int_fertile_focal_set = set(fertile_focal_count_AA)
	int_final_sterile_XA_set = set(final_sterile_XA_list)
	
	final_fertile_focal_list = list(int_fertile_focal_set - int_final_sterile_XA_set)

	combined_fertile = set(fertile_count_XA + fertile_count_AA)
	combined_sterile_AA_set = set(combined_sterile_AA)
	combined_sterile_XA_set = set(final_sterile_XA_list)
	final_fertile_focal_set = set(final_fertile_focal_list)

	int_fertile_list = combined_fertile - combined_sterile_AA_set
	int_fertile_list2 = int_fertile_list - combined_sterile_XA_set
	int_fertile_list3 = int_fertile_list2 - final_fertile_focal_set
	final_fertile_list = list(int_fertile_list3)
	
	# Count groups for 2x2 fisher's exact test
	
	Fisher_SF = len(combined_sterile_AA)
	Fisher_SNF = len(final_sterile_XA_list)
	Fisher_FF = len(final_fertile_focal_list)
	Fisher_FNF = len(final_fertile_list)
	
	odds, pvalue = sp.fisher_exact([[Fisher_SF, Fisher_SNF], [Fisher_FF, Fisher_FNF]])

	# Return final p-value

	print(pvalue)

File.close()
