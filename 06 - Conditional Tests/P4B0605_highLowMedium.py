'''
High low medium

For each gene, print out a message giving the gene name and saying whether its AT content is high (greater than 0.65),
low (less than 0.45) or medium (between 0.45 and 0.65).
'''


def highLowMedium(seq):
    length = len(seq)
    a_count = seq.upper().count('A')
    t_count = seq.upper().count('T')
    at_content = (a_count + t_count) / length
    return at_content

if __name__ == '__main__':
    with open('data.csv') as f:
        for line in f:
            columns = line.rstrip("\n").split(",")
            species = columns[0]
            sequence = columns[1]
            name = columns[2]
            expression = columns[3]

            if highLowMedium(sequence) > 0.65:
                print(name + " has high AT content")
            elif highLowMedium(sequence) < 0.45:
                print(name + " has low AT content")
            else:
                print(name + " has medium AT content")





