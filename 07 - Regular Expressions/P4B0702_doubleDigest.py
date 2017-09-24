'''
Download a file dna.txt which contains a made up DNA sequence.
Predict the fragment lengths that we will get if we digest the sequence with two made up restriction enzymes
– AbcI, whose recognition site is ANT/AAT, and AbcII, whose recognition site is GCRW/TG.
The forward slashes (/) in the recognition sites represent the place where the enzyme cuts the DNA.
N - any base
R - A or G
W - A or T
'''

import re

def doubleDigest(dna):
    print("DNA length is " + str(len(dna)))
    all_cuts = [0]

    # add cut positions for AbcI
    for m in re.finditer(r"A[ATGC]TAAT", dna):
        all_cuts.append(m.start() + 3)

    # add cut positions for AbcII
    for m in re.finditer(r"GC[AG][AT]TG", dna):
        all_cuts.append(m.start() + 4)

    # add the final position
    all_cuts.append(len(dna))
    sorted_cuts = sorted(all_cuts)
    print(sorted_cuts)

    for i in range(1, len(sorted_cuts)):
        this_cut_position = sorted_cuts[i]
        previous_cut_position = sorted_cuts[i - 1]
        fragment_size = this_cut_position - previous_cut_position
        print("one fragment size is  " + str(fragment_size))


if __name__ == '__main__':
    with open('dna.txt') as f:
        dna = f.read().rstrip("\n")
        print(doubleDigest(dna))
