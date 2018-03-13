def count_words():
    """count the number of words apparing in a string"""
    while True:
        filename = input("\nTell me which file you want to analize ('q' to stop) : ")
        if filename == 'q':
            break
        try:
            with open(filename) as file_object:
                content = file_object.read()
        except FileNotFoundError:
            print("Sorry, " + filename + " doesn't exist.")
        else:
            while True:
                word = input("\tNow, tell me which word you want to count ('q'to stop): ")
                if word == 'q':
                    break
                nbr_words = content.lower().count(word)
                print("\tThe file " + filename + " have " + str(nbr_words) + " times the word '" + word + "'.")

count_words()
