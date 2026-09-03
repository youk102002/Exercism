import math
def classify(number):
    """Classify a positive integer based on Nicomachus' classification scheme."""
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return "deficient"

    # 1 est toujours un diviseur propre pour number > 1
    aliquot_sum = 1

    # On cherche les diviseurs de 2 jusqu'à sqrt(number)
    limit = int(number**0.5)
    for i in range(2, limit + 1):
        if number % i == 0:
            aliquot_sum += i
            # On ajoute le facteur complémentaire s'il est différent de i
            if i != number // i:
                aliquot_sum += number // i

    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"
