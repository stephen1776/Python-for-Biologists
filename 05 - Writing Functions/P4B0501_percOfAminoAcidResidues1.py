'''
Percentage of amino acid residues, part one

Write a function that takes two arguments – a protein sequence and an amino acid residue code – and returns the
percentage of the protein that the amino acid makes up.

Use the following assertions to test your function:

assert my_function("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert my_function("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert my_function("msrslllrfllfllllpplp", "L") == 50
assert my_function("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
'''
import sys

def aminoAcidPercentage(protein, amino_acid):
    amino_acid_count = protein.count(amino_acid)
    protein_length = len(protein)
    percentage = (amino_acid_count / protein_length) * 100
    return percentage



if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    protein = lines[0].upper()
    amino_acid = lines[1].upper()
    print(aminoAcidPercentage(protein, amino_acid))
