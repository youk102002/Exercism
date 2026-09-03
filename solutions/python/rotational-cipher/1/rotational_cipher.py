import string
def rotate(text, key):
    key = key % 26
    lower = string.ascii_lowercase
    lower_shifted = lower[key:]+ lower[:key]
    upper = string.ascii_uppercase
    upper_shifted = upper[key:]+ upper[:key]

    table = str.maketrans(lower + upper, lower_shifted + upper_shifted)
       
    return text.translate(table)            
