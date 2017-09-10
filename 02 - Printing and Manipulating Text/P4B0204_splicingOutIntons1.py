'''
Splicing out introns, part one

Here's a short section of genomic DNA:

ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT

It comprises two exons and an intron. The first exon runs from the start of the sequence to base number 63
(starting counting from zero), and the second exon runs from base 91 (also counting from zero)
to the end of the sequence. Write a program that will print just the coding regions of the DNA sequence.
'''
import sys

def splicingOutIntrons1(dna):
    exon1 = dna[0:64]
    exon2 = dna[91:]

    return exon1 + exon2


if __name__ == '__main__':
    dna = sys.stdin.read().rstrip("\n")
    print(splicingOutIntrons1(dna))