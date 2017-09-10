'''
Restriction fragment lengths

Here's a short DNA sequence:

ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT

The sequence contains a recognition site for the EcoRI restriction enzyme, which cuts at the motif
G*AATTC
(the position of the cut is indicated by an asterisk).
Write a program which will calculate the size of the two fragments that will be produced when the DNA sequence
is digested with EcoRI.
'''

import sys

def restrictionFragmentLengths(dna):
    frag1_length = dna.find("GAATTC") + 1
    frag2_length = len(dna) - frag1_length
    frag_lengths = [frag1_length,frag2_length]

    return frag_lengths


if __name__ == '__main__':
    dna = sys.stdin.read().rstrip("\n")
    print(restrictionFragmentLengths(dna))