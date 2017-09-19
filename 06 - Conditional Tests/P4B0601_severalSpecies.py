'''
Click here to download a text file called data.csv, containing some made-up data for a number of genes.
Each line contains the following fields for a single gene in this order: species name, sequence, gene name,
expression level.
The fields are separated by commas (hence the name of the file – csv stands for Comma Separated Values).

Several species

Print out the gene names for all genes belonging to Drosophila melanogaster or Drosophila simulans.
'''



def severalSpecies(species, name):
    if species == "Drosophila melanogaster" or species == "Drosophila simulans":
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

            print(severalSpecies(species, name))