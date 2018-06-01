def abbreviate(words):
    words = words.upper()
    temp = ''
    looking_for_letter = True

    for char in words:
        if char.isalpha() and looking_for_letter:
            temp += char
            looking_for_letter = False
        elif not char.isalpha():
            looking_for_letter = True
    
    return temp
