def square_of_sum(number):
    number_list = [element for element in range(1, number + 1)]
    return sum(number_list)**2

def sum_of_squares(number):
    number_list = [element**2 for element in range(1, number + 1)]
    return sum(number_list)

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
