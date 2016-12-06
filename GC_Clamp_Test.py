#!/usr/bin/env python

# This is part of a sub-test included in my future "Primer Design Quick Test" 
# This sub-test will measure the "GC Clamp" of a given primer.
# The GC Clamp is the term I'm using to describe the presence of G or C bases within 
# the last five bases of the 3' end of a primer. As triple bonds exist between
# G and C basepairs and double bonds exist between A and T basepairs, a higher 
# presence of G's and C' will promote greater annealing of your primers to 
# complementary sequences than T and A basepairs.
# However, this effect can be deleterious if a run of G and C basepairs occurs at the
# 3' end of the primer sequence.  Specifically, primer dimer 

print('Welcome to the Primer GC Clamp test. Please enter the primer you wish to test')

primer_entry = input("Paste sequence here:\n").upper()


seq = primer_entry
assert len(seq) == (seq.count('U') + seq.count('C') + seq.count('A') + seq.count('G')), "Sequence is invalid, please enter a valid sequence" 

seq2 = seq[-5:]
gc_clamp = float(seq2.count('G') + seq2.count('C'))

if gc_clamp > 3
    
