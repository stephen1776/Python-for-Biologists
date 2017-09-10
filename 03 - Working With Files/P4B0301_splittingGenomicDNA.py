'''
Splitting genomic DNA

Look at the file called genomic_dna.txt – it contains the same piece of genomic DNA that we were using in the final
exercise from the previous page.

Write a program that will split the genomic DNA into coding and non-coding parts, and write these sequences
to two separate files.
'''


def splittingGenomicDNA():
    exon1 = dna[0:64]
    intron = dna[64:91].lower()
    exon2 = dna[91:]

    return [exon1 + exon2, intron]


if __name__ == '__main__':
    with open('genomic_dna.txt') as f:
        dna = f.read()
    with open('coding_part.txt','w') as cp:
        cp.write(splittingGenomicDNA()[0])
    with open('noncoding_part.txt', 'w') as ncp:
        ncp.write(splittingGenomicDNA()[1])
