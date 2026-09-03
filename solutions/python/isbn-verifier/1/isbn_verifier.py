def is_valid(isbn):
    clean_isbn = isbn.replace("-", "")

    if len(clean_isbn) != 10:
        return False

    # Validation de la structure : 9 chiffres + (1 chiffre ou X)
    if not (clean_isbn[:-1].isdigit() and (clean_isbn[-1].isdigit() or clean_isbn[-1] == "X")):
        return False

    # Transformation du dernier caractère ('X' -> 10)
    values = [int(c) if c != "X" else 10 for c in clean_isbn]

    # Somme pondérée de 10 à 1
    return sum(val * weight for val, weight in zip(values, range(10, 0, -1))) % 11 == 0