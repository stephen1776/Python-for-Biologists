'''
AT content

Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200.
'''



def atContent(seq):
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
            expression = int(columns[3])
            if atContent(sequence) < 0.5 and expression > 200:
                print(name)