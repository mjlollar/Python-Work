import sys

# This script serves the purpose of testing primers for efficacy using a realtively 
# simple algorithm.

print('Welcome to the Primer GC content test. Please enter or the primer you wish to test or enter "README" for more information.')

while True:
	primer_entry = input("Paste sequence here:\n").upper()
	if primer_entry in ['README']:
		print("More information coming soon")
	else:
	    break	
def validate_base_sequence(primer_entry):
    seq = primer_entry
    assert len(seq) == seq.count('U') + seq.count('C') + seq.count('A') + seq.count('G'), "Sequence is invalid, please enter a valid sequence"
def gc_content(primer_entry):
    seq = primer_entry
    return (seq.count('G') + seq.count('C')) / len(seq)
	

print("Your GC content is:\n")
print(gc_content(primer_entry))