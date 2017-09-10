'''
Writing a FASTA file

Write a program that will create a FASTA file for the following three sequences –
make sure that all sequences are in uppercase and only contain the bases A, T, G and C.

Sequence header 	DNA sequence
ABC123 	ATCGTACGATCGATCGATCGCTAGACGTATCG
DEF456 	actgatcgacgatcgatcgatcacgact
HIJ789 	ACTGAC-ACTGT--ACTGTA----CATGTG
'''

def writeFASTA():
    seq_header1 = "ABC123"
    seq_header2 = "DEF456"
    seq_header3 = "HIJ789"

    seq1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
    seq2 = "actgatcgacgatcgatcgatcacgact"
    seq3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

    return [seq_header1, seq_header2, seq_header3, seq1, seq2.upper(), seq3.replace('-', '')]


if __name__ == '__main__':
    with open('dna_sequences.fasta', 'w') as dsf:
        dsf.write('>' + writeFASTA()[0] + '\n')
        dsf.write(writeFASTA()[3] + '\n')
        dsf.write('>' + writeFASTA()[1] + '\n')
        dsf.write(writeFASTA()[4] + '\n')
        dsf.write('>' + writeFASTA()[2] + '\n')
        dsf.write(writeFASTA()[5] + '\n')

