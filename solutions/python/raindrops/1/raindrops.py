""" Convert a number into its corresponding raindrop sounds. """
def convert(number):
    """
    Function convert a number into its corresponding raindrop sounds. 

    Parameters : 
        number : given number

    Return: 
        is divisible by 3, add "Pling" to the result.
        is divisible by 5, add "Plang" to the result.
        is divisible by 7, add "Plong" to the result.
        is not divisible by 3, 5, or 7, the result should be the number as a string.
    """
    sound = ""
    if number % 3 == 0 :
        sound = sound + "Pling"
    if number % 5 == 0 :
        sound = sound + "Plang"
    if number % 7 == 0 :
        sound = sound + "Plong"
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0 :
        sound = sound + str(number)
    return sound
