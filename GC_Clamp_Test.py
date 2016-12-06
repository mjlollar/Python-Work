#!/usr/bin/env python

# This is part of a sub-test included in my future "Primer Design Quick Test" 
# This sub-test will measure the "GC Clamp" of a given primer.
# The GC Clamp is a term used to describe the presence of G or C bases within 
# the last five bases from the 3' end of primers. As triple bonds exist between
# G and C basepairs and double bonds exist between A and T basepairs, the 
# presence of G's and C's at this region of your primer will aid in the 
# annealling probability of your primers.

print('Welcome to the Primer GC content test. Please enter the primer you wish to test')

primer_entry = input("Paste sequence here:\n").upper()


seq = primer_entry
assert len(seq) == (seq.count('U') + seq.count('C') + seq.count('A') + seq.count('G')), "Sequence is invalid, please enter a valid sequence" 
