'''
Here's a dict which represents the genetic code – the keys are codons and the values are amino acid residues:


Copy and paste this chunk of code into a new program, then use this dict to write a program which will translate a
DNA sequence into protein. You'll have to figure out how to:

    split the DNA sequence into codons
    look up the amino acid residue for each codon
    join all the amino acids to give a protein

'''



def DNA_Translation(gencode, dna):
    last_codon_start = len(dna) - 2
    protein = ""
    for i in range(0,last_codon_start,3):
        codon = dna[i : i+3]
        aa = gencode.get(codon, 'X')
        protein = protein + aa
    return protein

if __name__ == '__main__':
    gencode = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}


    DNA1 = "ATGTTCGGT" # Translates to MFG
    DNA2 = "ATCGATCGAT" # Translates to IDR
    DNA3 = "ACGANCGAT" # Translates to TXD
    print("DNA sequence " + DNA1 + ", translates to protein sequence " + DNA_Translation(gencode, DNA1))
    print("DNA sequence " + DNA2 + ", translates to protein sequence " + DNA_Translation(gencode, DNA2))
    print("DNA sequence " + DNA3 + ", translates to protein sequence " + DNA_Translation(gencode, DNA3))
