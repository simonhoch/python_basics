favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(name.title() + ' favorite language is ' +
       language.title() + '.')
       
print('\n')

friends = ['phil', 'sarah']

for name in favorite_languages:
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title()+ "!")

if 'erin' not in favorite_languages:
    print("Erin, please take our poll!")

print('\n')

for name in sorted(favorite_languages):
    print(name.title() + ',thank u for  taking the poll.')

print ('\nThe following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())

print('\n')

print ('\nThe following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())
print('...')

favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
    print('\n' + name.title() + ' favorite language is:')
    for language in languages:
        print('\t' + language.title())
