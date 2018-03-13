#playing with strings : case, composing print, blank
name = "ada lovelace"
print (name.title())
name = "Ada Lovelace"
print (name.upper())
print (name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print (full_name)

message = "hello, " + full_name.title() + "!"
print (message)

print("\nPython\n\tC\n\tJavaScript")
#remove blank
favorite_language = ' python '
favorite_language = favorite_language.rstrip()
favorite_language = favorite_language.lstrip()
print (favorite_language)
