#!/usr/bin/env python

print('Welcome to the Primer GC content test. Please enter the primer you wish to test')

primer_entry = input("Paste sequence here:\n").upper()


seq = primer_entry
assert len(seq) == (seq.count('U') + seq.count('C') + seq.count('A') + seq.count('G')), "Sequence is invalid, please enter a valid sequence" 
	
gc_content = float((seq.count('G') + seq.count('C')) / len(seq)) * 100

print("Your GC content is:\n")
print(str(gc_content) + "%")

while True:
    if gc_content >= 50.0:
        print("This GC content is within acceptable range!")
        break
    else:
        print("This GC content is too low!")
        break
