def square(number):
    """
    number : the square number
    return the number of grains on a given square
    raise an error if number is not in range 1-64
    """
    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    """
    return the number of grains on a the chessboard
    """
    return 2 ** 64 - 1
