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






