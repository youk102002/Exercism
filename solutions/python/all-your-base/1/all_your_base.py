def rebase(input_base, digits, output_base):
    # 1. Validation des bases
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # 2. Validation des chiffres
    for digit in digits:
        if not (0 <= digit < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # 3. Conversion de la input_base vers un entier décimal unique
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * input_base + digit

    # Cas particulier : le nombre vaut 0
    if decimal_value == 0:
        return [0]

    # 4. Conversion de l'entier décimal vers la output_base
    output_digits = []
    while decimal_value > 0:
        output_digits.append(decimal_value % output_base)
        decimal_value //= output_base

    return output_digits[::-1]