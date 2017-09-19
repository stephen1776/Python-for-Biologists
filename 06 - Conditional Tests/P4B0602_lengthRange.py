'''
Length range

Print out the gene names for all genes between 90 and 110 bases long.
'''

def lengthRange(species, name):
    if len(sequence) > 90 and len(sequence) < 110:
        return name
    else:
        return ""


if __name__ == '__main__':
    with open('data.csv') as f:
        for line in f:
            columns = line.rstrip("\n").split(",")
            species = columns[0]
            sequence = columns[1]
            name = columns[2]
            expression = columns[3]

            print(lengthRange(species, name))