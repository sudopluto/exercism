import string

def is_pangram(sentence):
    letters = set(string.ascii_lowercase)
    return is_panagram_help(sentence.lower(), letters)

def is_panagram_help(sentence, letters):
    print(letters)
    if len(letters) == 0:
        return True
    elif len(sentence) == 0:
        return False
    else:
        letters.discard(sentence[0])
        return is_panagram_help(sentence[1:], 
                    letters)

