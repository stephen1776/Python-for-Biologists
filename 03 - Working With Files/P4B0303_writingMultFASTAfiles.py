'''
Writing multiple FASTA files

Use the data from the previous exercise, but instead of creating a single FASTA file, create three new FASTA files –
one per sequence. The names of the FASTA files should be the same as the sequence header names,
with the extension .fasta.
'''


def writeMultiFASTA():
    seq_header1 = "ABC123"
    seq_header2 = "DEF456"
    seq_header3 = "HIJ789"

    seq1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
    seq2 = "actgatcgacgatcgatcgatcacgact"
    seq3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

    return [seq_header1, seq_header2, seq_header3, seq1, seq2.upper(), seq3.replace('-', '')]


if __name__ == '__main__':
    with open('dna_sequences_1.fasta', 'w') as dsf1:
        dsf1.write('>' + writeMultiFASTA()[0] + '\n')
        dsf1.write(writeMultiFASTA()[3] + '\n')
    with open('dna_sequences_2.fasta', 'w') as dsf2:
        dsf2.write('>' + writeMultiFASTA()[1] + '\n')
        dsf2.write(writeMultiFASTA()[4] + '\n')
    with open('dna_sequences_3.fasta', 'w') as dsf3:
        dsf3.write('>' + writeMultiFASTA()[2] + '\n')
        dsf3.write(writeMultiFASTA()[5] + '\n')

