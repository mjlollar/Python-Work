# Same Power analysis for sterility QTLs with added penetrance simulator
# Penetrence of sterility is set at 50% for non-focal and focal two-allele sterile combination
# In case that real penetrance of sterility is near 100%, this simulator is also a conservative
# estimate of cases in which sterile loci display heterozygosity in parental population


import sys
import csv
import scipy.stats as sp
import itertools as it
import random as ran

csv.register_dialect('tab_delim', delimiter="\t", quoting=csv.QUOTE_NONE)

file_name = sys.argv[1] 

def read_lines(csv_reader, row_list):
	for row_number, row in enumerate(csv_reader):
		if row_number in row_list:
			yield row_number, row

with open(file_name, 'r') as File:
	replicate_list = []
	reader = csv.reader(File, dialect='tab_delim')
	window1 = list(range(0, 500))
  
	for row_number, row in read_lines(reader, window1):
		row_tuples = list(it.combinations(row, 2))
		replicate_list.append(row_tuples)

	window_list = list(map(list, zip(*replicate_list)))
	window_sterileXA = window_list[25000]
	counted_window_sterile_XA = list(enumerate(window_sterileXA))
	window_sterileAA = window_list[79800]
	counted_window_sterile_AA = list(enumerate(window_sterileAA))
	
	sterile_count_AA = []
	fertile_count_AA = []
	fertile_focal_count_AA = []

	for window in counted_window_sterile_AA:
		if window[1] == ('0', '2'):
			value = ran.randint(0, 1)
			prob = value
			if prob == 1:
				sterile_count_AA.append(window[0])
			else:
				fertile_focal_count_AA.append(window[0])
		else:
			fertile_count_AA.append(window[0])	
	
	sterile_count_XA = []
	fertile_count_XA = []

	for window in counted_window_sterile_XA:
		if window[1] == ('0', '2'):
			value = ran.randint(0, 1)
			prob = value
			if prob ==1:
				sterile_count_XA.append(window[0])
			else:
				fertile_count_XA.append(window[0])
		else:
			fertile_count_XA.append(window[0])

	
	sterile_XA_set = set(sterile_count_XA)
	sterile_AA_set = set(sterile_count_AA)
	int_sterile_XA_list = sterile_XA_set - sterile_AA_set
	
	final_sterile_XA_list = list(int_sterile_XA_list)

	
	combined_fertile = set(fertile_count_XA + fertile_count_AA)
	fertile_focal_set = set(fertile_focal_count_AA)
	int_fertile_list = combined_fertile - int_sterile_XA_list
	int_fertile_list2 = int_fertile_list - fertile_focal_set
	
	final_fertile_list = list(int_fertile_list2)

	Fisher_SF = len(sterile_count_AA)
	Fisher_SNF = len(final_sterile_XA_list)
	Fisher_FF = len(fertile_focal_count_AA)
	Fisher_FNF = len(final_fertile_list)
	
	odds, pvalue = sp.fisher_exact([[Fisher_SF, Fisher_SNF], [Fisher_FF, Fisher_FNF]])

	print(pvalue)

File.close()



