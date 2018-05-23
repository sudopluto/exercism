# Score categories
# Change the values as you see fit

from functools import reduce

YACHT = (lambda l: 50 if len(set(l)) == 1 else 0)
ONES = (lambda l: len(list(filter((lambda e: e == 1), l))))
TWOS = (lambda l: len(list(filter((lambda e: e == 2), l))) * 2)
THREES = (lambda l: len(list(filter((lambda e: e == 3), l))) * 3)
FOURS = (lambda l: len(list(filter((lambda e: e == 4), l))) * 4)
FIVES = (lambda l: len(list(filter((lambda e: e == 5), l))) * 5)
SIXES = (lambda l: len(list(filter((lambda e: e == 6), l))) * 6)
FULL_HOUSE = (lambda l: CHOICE(l) if len(set(l)) == 2 
                                    and (l.count(l[0]) == 3
                                        or l.count(l[0]) == 2)
                        else 0)
FOUR_OF_A_KIND = (lambda l: 4 * sorted(l)[1]  if len(set(l)) <= 2 
                                    and (l.count(l[0]) >= 4
                                        or l.count([0]) <= 1)
                        else 0)
LITTLE_STRAIGHT = (lambda l: 30 if len(set(l)) == 5 
                                    and (sorted(l)[0] == 1 
                                        and sorted(l)[-1] == 5)
                        else 0)
BIG_STRAIGHT = (lambda l: 30 if len(set(l)) == 5 
                                    and (sorted(l)[0] == 2 
                                        and sorted(l)[-1] == 6)
                        else 0)
CHOICE = (lambda l: reduce((lambda e, a: a + e), l))


def score(dice, category):
    return category(dice)

