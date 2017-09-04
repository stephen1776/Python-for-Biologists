'''
Splicing out introns, part two
dna =
ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
Using the data from part one, write a program that will calculate what percentage of the DNA sequence is coding.
'''
import sys

def splicingOutIntrons2(dna):
    exon1 = dna[0:64]
    exon2 = dna[91:]
    coding_length = len(exon1 + exon2)
    total_length = len(dna)

    return 100 * coding_length / total_length


if __name__ == '__main__':
    dna = sys.stdin.read().rstrip("\n")
    print(splicingOutIntrons2(dna))