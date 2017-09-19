'''
Complex condition

Print out the gene names for all genes whose name begins with "k" or "h" except those belonging to
Drosophila melanogaster.
'''


def complexCondition(species, name):
    if (name.startswith('k') or name.startswith('h')) and species != "Drosophila melanogaster":
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

            print(complexCondition(species, name))