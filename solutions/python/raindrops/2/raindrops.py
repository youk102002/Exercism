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
    raindrop_sound = ""
    sounds = [(3,"Pling"),(5,"Plang"),(7,'Plong')]
    for (factor, sound) in sounds :
        if number % factor == 0 :
            raindrop_sound = raindrop_sound + sound
    return raindrop_sound if raindrop_sound != "" else str(number)