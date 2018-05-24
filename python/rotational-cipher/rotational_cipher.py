def rotate(text, key):
    num_letters = 26
    key = key % num_letters
    l_min = ord('a')
    u_min = ord('A')


    text = list(
            map((lambda s: 
                        s if not s.isalpha()
                        else chr(l_min + (((ord(s) - l_min) + key) % num_letters))
                                if s.islower()
                        else chr(u_min + (((ord(s) - u_min) + key) % num_letters))),
                list(text)))
    return ''.join(text)
