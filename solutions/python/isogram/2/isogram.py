"""Determine if a word or phrase is an isogram."""
def is_isogram(phrase):
    phrase = phrase.lower()
    alphabet = {}
    for letter in phrase :
        if letter.isalpha(): 
            if alphabet.get(letter) is None :
                alphabet[letter] = 0
            else :
                return False
    return True
