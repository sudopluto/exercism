import re

def word_count(phrase):
    word_hist = {}
    phrase = phrase.lower()

    phrase_as_list = re.split(r'[^a-zA-Z0-9\'"]', phrase)

    phrase_as_list = list(filter(None, phrase_as_list))
    phrase_as_list = list(map((lambda x: x.strip('\'"')), phrase_as_list))

    for word in phrase_as_list:
        word_hist[word]= word_hist.get(word, 0) + 1

    return word_hist
