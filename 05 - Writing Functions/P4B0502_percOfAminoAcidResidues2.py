'''
Percentage of amino acid residues, part two

Modify the function from part one so that it accepts a list of amino acid residues rather than a single one.
If no list is given, the function should return the percentage of hydrophobic amino acid residues
(A, I, L, M, F, W, Y and V).

Your function should pass the following assertions:

assert my_function("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert my_function("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert my_function("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert my_function("MSRSLLLRFLLFLLLLPPLP") == 65
'''


def aminoAcidPercentage2(protein, amino_acid_list = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    protein = protein.upper()
    protein_length = len(protein)
    total_count = 0
    for i in amino_acid_list:
        i = i.upper()
        amino_acid_count = protein.count(i)
        total_count += amino_acid_count
    percentage = (total_count / protein_length) * 100
    return percentage

print(aminoAcidPercentage2("MSRSLLLRFLLFLLLLPPLP", ["M"]) )
print(aminoAcidPercentage2("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) )
print(aminoAcidPercentage2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) )
print(aminoAcidPercentage2("MSRSLLLRFLLFLLLLPPLP") )
