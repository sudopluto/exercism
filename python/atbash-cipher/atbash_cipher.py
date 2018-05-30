def encode(plain_text):
    encoded = ''
    chuncksize = 5
    
    
    for char in plain_text.lower():
        encoded += flip(char)
        
    chuncked = ''
    counter = chuncksize

    for char in encoded:
        chuncked += char
        counter -= 1
        if counter == 0:
            chuncked += ' '
            counter = chuncksize
    
    if chuncked[-1] == ' ':
        chuncked = chuncked[:-1]
    
    return chuncked


def decode(ciphered_text):
    temp = ''
    for char in ciphered_text.lower():
        temp += flip(char)
    return temp

def flip(char):
    lower_base = ord('a')
    alphabet_size = 25

    if char.islower():
        return chr(alphabet_size -(ord(char) - lower_base) 
                    + lower_base)
    elif char in ',._ ':
        return ''
    else:
        return char
