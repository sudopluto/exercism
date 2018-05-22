import re

def hey(phrase):

    phrase = re.sub(r'[^a-zA-Z0-9?]', '', phrase)

    if len(phrase) == 0:
        return "Fine. Be that way!"
    elif phrase.isupper() and phrase[-1] == '?':
        return 'Calm down, I know what I\'m doing!'
    elif phrase[-1] == '?':
        return 'Sure.'
    elif phrase.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'