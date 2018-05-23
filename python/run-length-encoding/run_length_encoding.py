def decode(string):

    if string == '' :
        return ''
    else:
        first_letter_i = [x.isalpha() or x == ' ' for x in string].index(True)
        mult = 1
        if string[0:first_letter_i].isdigit():
            mult = int(string[0:first_letter_i])

        return string[first_letter_i] * mult + decode(string[first_letter_i+1:])

def encode(string):
    
    current_char = '' 
    current_count = 0
    builder = ''

    for char in string:

        if char != current_char:
            if current_count != 0:
                if current_count == 1:
                    builder += '%s' % (current_char)
                else:
                    builder += '%d%s' % (current_count, current_char)
            current_char = char
            current_count = 1
        else:
            current_count += 1
            
    if current_count != 0:
            if current_count == 1:
                    builder += '%s' % (current_char)
            else:
                builder += '%d%s' % (current_count, current_char)

    return builder
