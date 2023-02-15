# help(str)
# Use upper()


def print_upper_words(words):
    """ Print all words in a list in upper case, each on a seperate line
    """
    for word in words:
        print(word.upper())


# this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])


def print_upper_words_e(words):
    """ Print all words in a list in upper case, each on a seperate line and must start with the letter e.
    """
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


# this should print "ELLO"

# print_upper_words_e(["hello", "hey", "goodbye", "yo", "yes", "ello"])


def print_upper_words_only(words, must_start_with):
    """ Print all words in a list in upper case, each on a seperate line and must start with the letter e.
    """
    for word in words:
        if any(word.startswith(letter) for letter in must_start_with):
            print(word.upper())


# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words_only(["hello", "hey", "goodbye", "yo", "yes"],
                       must_start_with={"h", "y"})
