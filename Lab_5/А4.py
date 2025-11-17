def genetic_data(filename):
    data = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            protein_data = (
                parts[0].strip(),
                parts[1].strip(),
                parts[2].strip()
            )
            data.append(protein_data)
        return data

def read_commands(filename):
    commands = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            command = (
                parts[0].strip(),
                parts[1].strip()
            )
            commands.append(command)
        return commands

def decode(word):
    result = ''
    i = 0
    while i < len(word):
        if word[i].isdigit():
            result += word[i + 1] * int(word[i])
            i += 1
        else:
            result += word[i]
        i += 1
    return result

def search(data, amino_sequence):
    for sequence in data:
        if amino_sequence in sequence[2]:
            return f'organism\t\t\t\tprotein\n{sequence[1]}\t{sequence[0]}'
    return 'NOT FOUND'

def diff(data, protein1, protein2):
    seq1 = seq2 = None
    for protein in data:
        if protein[0] == protein1:
            seq1 = protein[2]
        elif protein[0] == protein2:
            seq2 = protein[2]

    if seq1 is None and seq2 is None:
        return f"MISSING: {protein1}, {protein2}"
    elif seq1 is None:
        return f"MISSING: {protein1}"
    elif seq2 is None:
        return f"MISSING: {protein2}"

    min_length = min(len(seq1), len(seq2))
    difference = 0
    for i in range(min_length):
        if seq1[i] != seq2[i]:
            difference += 1
    difference = difference + abs(len(seq1) - len(seq2))
    return str(difference)







