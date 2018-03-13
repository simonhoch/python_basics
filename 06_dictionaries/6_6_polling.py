favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['jen', 'sophie', 'sarah', 'simon',  'sacho', 'rumi']

for person in people:
    if person in favorite_languages:
        print('Thanks ' + person.title() + ', for taking the roll')
    else :
        print('Please ' + person.title() + ', could you take the roll?')
