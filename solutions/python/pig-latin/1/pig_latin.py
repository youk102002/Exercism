"""  Translate text from English to Pig Latin """
def translate(text):
    vowels = ("a", "e", "i", "o", "u")
    
    def translate_word(word):
        # Rule 1: Mot commence par une voyelle, "xr" ou "yt"
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            return word + "ay"
        
        # Helper pour trouver où couper le mot (Règles 2, 3 et 4)
        def trouver_indice(w):
            for i in range(len(w)):
                # Rule 3: "qu" précédé de 0 ou plusieurs consonnes
                if i < len(w) - 1 and w[i] == "q" and w[i + 1] == "u":
                    return i + 2  # On coupe après le 'u'
                
                # Rule 4: 'y' précédé d'au moins une consonne (i > 0)
                if w[i] == "y" and i > 0:
                    return i      # On coupe avant le 'y'
                
                # Rule 2: Premier 'a, e, i, o, u' rencontré
                if w[i] in vowels:
                    return i      # On coupe avant la voyelle
            return 0

        i = trouver_indice(word)
        # Découpage : préfixe de consonnes et le reste du mot
        return word[i:] + word[:i] + "ay"

    # Traitement mot par mot pour gérer les phrases complètes
    words = text.split()
    translated_words = [translate_word(word) for word in words]
    return " ".join(translated_words)