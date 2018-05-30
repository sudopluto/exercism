from functools import reduce

def sum_of_multiples(limit, multiples):
    
    list_of_mults = []
    
    for num in range(limit):
        if reduce((lambda i, e: i or num % e == 0), multiples, False):
            list_of_mults.append(num)
    
    print(list_of_mults)
    return reduce((lambda i, e: i + e), list_of_mults, 0)
