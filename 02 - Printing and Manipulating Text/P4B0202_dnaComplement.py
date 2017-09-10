# Complementing DNA
#
# Here's a short DNA sequence:#
# ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
# Write a program that will print the complement of this sequence.
# Replace A with T, T with A, C with G, and G with C
import sys

def dnaComplement(dna):
    dnaComplementDict = {'A':'T','C':'G','G':'C','T':'A'}  # create dictionary
    complementDNA = [dnaComplementDict[i] for i in dna]  # complement the dna
    complementDNA = complementDNA[::1]  #  the complement

    return complementDNA


if __name__ == '__main__':
    dna = sys.stdin.read().rstrip("\n")
    print(''.join(dnaComplement(dna)))


