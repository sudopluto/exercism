def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError('size too big')
    elif size == 0:
        return 1
    else:
        return largest_product_help(series, size, 0)

def largest_product_help(series, size, max):
    if len(series) < size:
        return max
    else:
        tempMax = 1
        for i in series[:size]:
            tempMax *= int(i)
        if tempMax > max:
            max = tempMax
        return largest_product_help(series[1:], size, max)
