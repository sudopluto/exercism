def detect_anagrams(word, candidates):
    temp_list = []

    for cand in candidates:
        if word.lower() == cand.lower():
            pass
        elif gen_hist(word.lower()) == gen_hist(cand.lower()):
            temp_list.append(cand)
    
    return temp_list

def gen_hist(word):
    
    emp_dict = {}

    for c in word:
        emp_dict[c] = emp_dict.get(c, 0) + 1
    
    return emp_dict
