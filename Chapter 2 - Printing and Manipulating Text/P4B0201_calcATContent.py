# Calculating AT Content
'''
Write a program that will print out the AT content of this DNA sequence (i.e. the proportion of bases that are either A or T).
'''
import sys

def calcATContent(dna):
    a_count = dna.count('A')
    t_count = dna.count('T')
    total_count = len(dna)
    at_content = (a_count + t_count) / total_count
    return at_content


if __name__ == '__main__':
    dna = sys.stdin.read().rstrip("\n")
    print(calcATContent(dna))
# use dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
