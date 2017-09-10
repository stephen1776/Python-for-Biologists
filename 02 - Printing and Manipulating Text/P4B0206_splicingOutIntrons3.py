'''
Splicing out introns, part three

Using the data from part one, write a program that will print out the original genomic DNA sequence
with coding bases in uppercase and non-coding bases in lowercase.
dna =
ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
'''
import sys

def splicingOutIntrons3(dna):
    exon1 = dna[0:64]
    intron = dna[64:91].lower()
    exon2 = dna[91:]

    return exon1 + intron + exon2


if __name__ == '__main__':
    dna = sys.stdin.read().rstrip("\n")
    print(splicingOutIntrons3(dna))