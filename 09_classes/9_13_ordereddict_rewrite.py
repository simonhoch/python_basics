from collections import OrderedDict

glossary = OrderedDict()

#glossary = {
#    'if': 'statement',
#    'for': 'loop',
#    'str': 'string',
#    'int': 'integer',
#    'list': 'items',
#   'dict': 'dictionnary',
#    }
glossary['.upper()'] = 'changing all letter in capital one'
glossary['if'] = 'statement'
glossary['for'] = 'loop'

for word, meaning in glossary.items():
    print (word + ' means in python ' + meaning)
