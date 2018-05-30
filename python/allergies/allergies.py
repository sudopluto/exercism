import math

class Allergies(object):

    KEY_OF_ALLERGIES = {
        0 : 'eggs',
        1 : 'peanuts',
        2 : 'shellfish',
        3 : 'strawberries',
        4 : 'tomatoes',
        5 : 'chocolate',
        6 : 'pollen',
        7 : 'cats'
    }

    def __init__(self, score):
        self.score = score
        self._lst = self.gen_list(score)

    def is_allergic_to(self, item):
        return item in self._lst

    def gen_list(self, score, built_list=None):
        if built_list == None:
            built_list = []

        if score <= 0:
            return built_list
        else:
            low_pow_two = math.floor(math.log(score,2))
            if low_pow_two in self.KEY_OF_ALLERGIES:
                built_list.append(self.KEY_OF_ALLERGIES[low_pow_two])
            return self.gen_list(score - 2 ** low_pow_two, built_list)
            

    @property
    def lst(self):
        return self._lst