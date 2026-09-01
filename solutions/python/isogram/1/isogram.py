def is_isogram(phrase):
    phrase = phrase.lower()
    alphabet = {}
    for letter in phrase :
        if letter.isalpha(): 
            if alphabet.get(letter) == None :
                alphabet[letter] = 0
            else :
                return False
    return True
