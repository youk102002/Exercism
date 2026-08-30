"""Module providing a function Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture."""
def steps(number):
    """Calculate the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.
 
    Parameters:
        number : a positive integer
 
    Returns:
        steps : the number of steps.
 
    Examples:
        >>> steps(12):
        9
 
    This function calculates the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.
    """
    if number < 1 :
        raise ValueError("Only positive integers are allowed")
        
    number_step = 0

    while number > 1 :
        number = (number / 2) if (number % 2 == 0) else (number * 3 + 1)
        number_step += 1
    
    return number_step    
