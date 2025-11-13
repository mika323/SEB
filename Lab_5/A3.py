def abbreviation(line):
    line = line.upper().split()
    st = ''
    for word in line:
        if len(word) < 3:
            continue
        else:
            st += word[0]
    return st

text = input('Введите текст: ')
print(abbreviation(text))











