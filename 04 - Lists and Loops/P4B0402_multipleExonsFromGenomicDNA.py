'''
Multiple exons from genomic DNA

The file genomic_dna.txt contains a section of genomic DNA, and the file exons.txt contains a list of start/stop
positions of exons. Each exon is on a separate line and the start and stop positions are separated by a comma.
The start and stop positions follow Python conventions;
they start from zero and are inclusive at the start and exclusive at the end.

Write a program that will extract the exon segments, concatenate them, and write them to a new file.
This is a tricky exercise with several parts: your program will have to:

    read the exon file line by line
    split each exon line into two numbers
    turn those numbers into integers
    extract the matching part of the genomic DNA sequence
    concatenate all the exon sequences together

'''

def multipleExons():
    coding_sequence = ''
    for line in exon_locations:
        # split the line using a comma
        positions = line.split(',')

        # get the start and stop positions
        start = int(positions[0])
        stop = int(positions[1])

        # extract the exon from the genomic dna
        exon = genomic_dna[start:stop]

        # append the exon to the end of the current coding sequence
        coding_sequence = coding_sequence + exon
    return coding_sequence



if __name__ == '__main__':
    with open('genomic_dna.txt') as g:
        genomic_dna = g.read()

    with open('exons.txt') as e:
        exon_locations = e.read().splitlines()

    with open('output_coding_sequence.txt', 'w') as ocs:
        ocs.write(multipleExons())
