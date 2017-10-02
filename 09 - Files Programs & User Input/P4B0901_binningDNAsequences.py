'''
Binning DNA sequences

Write a program which creates nine new folders – one for sequences between 100 and 199 bases long,
one for sequences between 200 and 299 bases long, etc.
Write out each DNA sequence in the input files to a separate file in the appropriate folder.

Your program will have to:

    iterate over the files in the folder
    iterate over the lines in each file
    figure out which bin each DNA sequence should go in based on its length
    write out each DNA sequence to a new file in the right folder

'''
import os

def binningDNAsequence(line, number):
    dna = line.rstrip("\n")
    length = len(dna)
    print("The sequence length is " + str(length))
    for bin_lower in range(100,1000,100):
        bin_upper = bin_lower + 99
        if length >= bin_lower and length < bin_upper:
            print("and the bin is " + str(bin_lower) + " to " + str(bin_upper))
            bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
            output_path = bin_folder_name + '/' + str(seq_number) + '.dna'
            output = open(output_path, "w")
            output.write(dna)
            output.close()

if __name__ == '__main__':
    for bin_lower in range(100, 1000, 100):
        bin_upper = bin_lower + 99
        bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
        os.mkdir(bin_folder_name)
    seq_number = 1
    for file_name in os.listdir("."):
        if file_name.endswith(".dna"):
            print("Now reading sequences from " + file_name)
            dna_file = open(file_name)
            for line in dna_file:
                binningDNAsequence(line, seq_number)
                seq_number = seq_number + 1



