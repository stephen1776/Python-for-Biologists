'''
Processing DNA in a file

The file input.txt contains a number of DNA sequences, one per line.
Each sequence starts with the same 14 base pair fragment – a sequencing adapter that should have been removed.
Write a program that will
(a) trim this adapter and write the cleaned sequences to a new file and
(b) print the length of each sequence to the screen.
'''

def processDNA():
    array_a = []
    for dna in dnas:

        # get substring from 15th character to end
        trim_adapter = dna[14:]

        # get seq length of trimmed sequence
        seq_length = len(trim_adapter) - 1
        array_a += [trim_adapter, seq_length]

    return array_a


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
        dnas = lines[0:4]
    with open('output_trimmedAdapter.txt', 'w') as ota:
        ota.write(processDNA()[0] + '\n' + processDNA()[2] + '\n' + processDNA()[4]+ '\n' + processDNA()[6])
    print(str(processDNA()[1]) + '\n' + str(processDNA()[3])+ '\n' + str(processDNA()[5])+ '\n' + str(processDNA()[7]) )