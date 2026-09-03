COLORS = {
    "black": 0, "brown": 1, "red": 2,
    "orange": 3, "yellow": 4, "green": 5,
    "blue": 6, "violet": 7, "grey": 8, "white": 9
}

def label(colors):
    """Calcule la valeur d'une résistance à 3 bandes de couleur."""
    # 1. On récupère les deux premiers chiffres et l'exposant
    first_digit = COLORS[colors[0]]
    second_digit = COLORS[colors[1]]
    power = COLORS[colors[2]]

    # 2. Valeur totale en ohms
    value = (first_digit * 10 + second_digit) * (10 ** power)

    # 3. Formatage de l'unité (du plus grand au plus petit avec >=)
    if value >= 10**9:
        return f"{value // 10**9} gigaohms"
    if value >= 10**6:
        return f"{value // 10**6} megaohms"
    if value >= 10**3:
        return f"{value // 10**3} kiloohms"
    
    return f"{value} ohms"
  
    
