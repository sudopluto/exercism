def is_isogram(string):
    return is_isogram_help(string.lower())
        
def is_isogram_help(string):
    if len(string) <= 1:
        return True
    elif not (string[0].isalpha()):
        return is_isogram_help(string[1:])
    else:
        print(string[0], string[1:])
        return (not (string[0] in string[1:])) and is_isogram_help(string[1:])
