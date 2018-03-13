glossary = {
    'if': 'statement',
    'for': 'loop',
    'str': 'string',
    'int': 'integer',
    'list': 'items',
    'dict': 'dictionnary',
    }
glossary['.upper()'] = 'changing all letter in capital one'

for word, meaning in glossary.items():
    print (word + ' means in python ' + meaning)
