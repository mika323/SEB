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
    amino_sequence = decode(amino_sequence)
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

def mode(data, protein):
    for line in data:
        if line[0] == protein:
            sequence = line[2]
            letters = {}
            for amino_acid in sequence:
                letters[amino_acid] = letters.get(amino_acid, 0) + 1
            max_value = max(letters.values())
            answer_letter = None
            for key in sorted(letters):
                if letters[key] == max_value:
                    max_value = letters[key]
                    answer_letter = key
                    break
            return answer_letter, max_value
    return 'MISSING'

data1 = genetic_data('sequences.0.txt')
file = open('genedata.txt', 'w', encoding = 'utf-8')
file.write('Milana Shastitko\n')
file.write('Genetic Searching\n')
file.write('-' * 74 + '\n')
commands_ = read_commands('commands.0.txt')
for index, command in enumerate(commands_):
    operation = command[0]
    param = command[1]
    if operation == 'search':
        result_ = search(data1, param)
        file.write(f'{index + 1:03d}   {operation}   {decode(param)}\n{result_}\n')
        file.write('-' * 74 + '\n')
        index += 1
    elif operation == 'diff':
        param1 = command[2]
        result_ = diff(data1, param, param1)
        file.write(f'{index + 1:03d}   {operation}   {param}   {param1}\namino-acids difference:\n{result_}\n')
        file.write('-' * 74 + '\n')
        index += 1
    elif operation == 'mode':
        result_ = mode(data1, param)
        file.write(f'{index + 1:03d}   {operation}   {param}\namino-acid occurs:\n{result_[0]}\t\t\t{result_[1]}\n')
        file.write('-' * 74 + '\n')
        index += 1











