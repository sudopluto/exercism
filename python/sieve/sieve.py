def sieve(limit):

    # generating a dict with all nums,
    # and their marked state
    list_of_nums = list(range(2,limit+1))
    mapping_of_nums = {}

    for num in list_of_nums:
        mapping_of_nums[num] = False

    for num in mapping_of_nums:
        if mapping_of_nums[num]:
            pass
        else:
            mult = 2
            while mult * num in mapping_of_nums:
                mapping_of_nums[mult * num] = True
                mult += 1
    
    result = []
    for num in mapping_of_nums:
        if not mapping_of_nums[num]:
            result.append(num)
            
    return result
