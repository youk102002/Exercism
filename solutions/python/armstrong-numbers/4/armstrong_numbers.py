def is_armstrong_number(number):
    """
        number : the number to check
        return : True if is Armstrong number 
    """
    digits = str(number)
    power = len(digits)
    armstrong = 0
    for  digit in digits:
        armstrong += int(digit) ** power
    return armstrong == number
