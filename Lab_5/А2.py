import re

text = 'He jests at scars. That never felt a wound!   Hello, friend!   Are you OK?'
sentences = re.split(r'(?<=[.?!]) +', text)

def print_sentences(items):
    for item in items:
        print(item)
        print()

print_sentences(sentences)
print(f'Предложений в тексте: {len(sentences)}')
