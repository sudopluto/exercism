def is_armstrong(number):
    return is_armstrong_acc(number, len(str(number)), 0) == number

def is_armstrong_acc(number, power, acc):
    if number == 0:
        return acc
    else:
        return is_armstrong_acc(number // 10, power, acc + (number % 10) ** power)