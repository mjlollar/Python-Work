#!/usr/bin/env python

# This is part of a sub-test included in my future "Primer Design Quick Test" 
# This sub-test will measure the "GC Clamp" of a given primer.
# The GC Clamp is the term I'm using to describe the presence of G or C bases within 
# the last five bases of the 3' end of a primer. As triple bonds exist between
# G and C basepairs and double bonds exist between A and T basepairs, a higher 
# presence of G's and C's will promote greater annealing of your primers to 
# complementary sequences than T and A basepairs, which share a double bond.
# However, this effect can be deleterious if a run of G and C basepairs occurs at the
# 3' end of the primer sequence.  Specifically, primer dimers are more likely to 
# occur if GC content in the 3' end is high.  A sweet spot seems to be around 2 or 
# so G's and C's in this region. Let's check out your GC Clamp!

print('Welcome to the Primer GC Clamp test. Please enter the primer you wish to test')

primer_entry = input("Paste sequence here:\n").upper()


seq = primer_entry
assert len(seq) == (seq.count('U') + seq.count('C') + seq.count('A') + seq.count('G')), "Sequence is invalid, please enter a valid sequence" 

seq2 = seq[-5:]
gc_clamp = float(seq2.count('G') + seq2.count('C'))

while True:
    if gc_clamp >= 3:
        print("The GC content at your 3' end is high. We suggest adjusting your primers")   
    elif gc_clamp == 2:
        print("Your GC content at the 3' end is fine.")
    else gc_clamp <= 1:
        print("Your GC content at the 3' end is low. This may not be a problem, but if possible we suggest adjusting your primer.")
        break
