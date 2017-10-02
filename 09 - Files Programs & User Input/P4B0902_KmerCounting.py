'''
Kmer counting

Write a program that will calculate the number of all kmers of a given length across all DNA sequences in the input
files and display just the ones that occur more than a given number of times.
Your program should take two command line arguments – the kmer length, and the cutoff number.
'''
import os
import sys

# define the function to split dna
def split_dna(dna, kmer_size):
    kmers = []
    for start in range(0,len(dna)-(kmer_size-1),1):
        kmer = dna[start:start+kmer_size]
        kmers.append(kmer)
    return kmers

if __name__ == '__main__':
    # try 6 23
    input = sys.stdin.read()
    
    kmer_size, count_cutoff = list(map(int, input.split()))

    # create an empty dictionary to hold the counts
    kmer_counts = {}

    # process each file with the right name
    for file_name in os.listdir("."):
        if file_name.endswith(".dna"):
            dna_file = open(file_name)

            # process each DNA sequence in a file
            for line in dna_file:
                dna = line.rstrip("\n")

                # increase the count for each k-mer that we find
                for kmer in split_dna(dna, kmer_size):
                    current_count = kmer_counts.get(kmer, 0)
                    new_count = current_count + 1
                    kmer_counts[kmer] = new_count

    # print k-mers whose counts are above the cutoff
    for kmer, count in kmer_counts.items():
        if count > count_cutoff:
            print(kmer + " : " + str(count))