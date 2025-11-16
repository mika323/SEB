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





