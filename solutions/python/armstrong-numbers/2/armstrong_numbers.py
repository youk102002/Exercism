def is_armstrong_number(number):
    digits = str(number)
    power = len(digits)
    sum = 0
    for  digit in digits:
        sum += int(digit) ** power
    return sum == number
