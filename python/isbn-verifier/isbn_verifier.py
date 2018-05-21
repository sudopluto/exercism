def verify(isbn):
    isbn = isbn.replace('-','')

    if len(isbn) != 10: return False
    
    isbn_as_list = []
    list_of_valid = [str(x) for x in range(0,10)]

    for dig in isbn[:-1]:
        if not dig in list_of_valid:
            return False
        else:
            isbn_as_list.append(int(dig))
    
    list_of_valid.append('X')

    if not isbn[-1] in list_of_valid:
        return False
    elif isbn[-1] == 'X':
        isbn_as_list.append(10)
    else:
        isbn_as_list.append(int(isbn[-1]))

    sum = 0

    for i in range (10, 0, -1):
        sum += isbn_as_list[10-i] * i
    
    return sum % 11 == 0
        





