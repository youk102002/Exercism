def is_armstrong_number(number):
    num_length = len(str(number))
    sum = 0;
    for x in range(num_length):
        sum += int(str(number)[x]) ** num_length
    return sum == number
