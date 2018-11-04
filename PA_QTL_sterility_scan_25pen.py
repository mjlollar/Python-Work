# Sterility QTL with Penetrance, added 250 scan.

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
	replicate_list_scan = []
	reader = csv.reader(File, dialect='tab_delim')
	window1 = list(range(0, 501))
	window2 = list(range(501, 751))
  
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
			prob = ran.randint(0, 3)
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
			prob = ran.randint(0, 3)
			if prob ==1:
				sterile_count_XA.append(window[0])
			else:
				fertile_count_XA.append(window[0])
		else:
			fertile_count_XA.append(window[0])

	File.seek(0)

	for row_number, row, in read_lines(reader, window2):
		row_tuples2 = list(it.combinations(row, 2))
		replicate_list_scan.append(row_tuples2)

	window_list2 = list(map(list, zip(*replicate_list_scan)))
	window_sterileXA_scan = window_list2[25000]
	counted_window_sterile_XA_scan = list(enumerate(window_sterileXA_scan, 501))
	window_sterileAA_scan = window_list2[79800]
	counted_window_sterile_AA_scan = list(enumerate(window_sterileAA_scan, 501))

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
			prob = ran.ranint(0, 3)
			if prob == 1:
				sterile_count_XA_scan.append(window[0])
			else:
				psss
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
	

	Fisher_SF = len(combined_sterile_AA)
	Fisher_SNF = len(final_sterile_XA_list)
	Fisher_FF = len(final_fertile_focal_list)
	Fisher_FNF = len(final_fertile_list)
	
	odds, pvalue = sp.fisher_exact([[Fisher_SF, Fisher_SNF], [Fisher_FF, Fisher_FNF]])

	print(pvalue)

File.close()
