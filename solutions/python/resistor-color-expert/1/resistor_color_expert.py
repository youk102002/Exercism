COLORS = {
    "black": 0, "brown": 1, "red": 2,
    "orange": 3, "yellow": 4, "green": 5,
    "blue": 6, "violet": 7, "grey": 8, "white": 9
}

TOLERANCES = {
    "grey": "0.05%", "violet": "0.1%", "blue": "0.25%", 
    "green": "0.5%", "brown": "1%", "red": "2%",
    "gold": "5%", "silver": "10%"
}

UNITS = [
    (10**9, "gigaohms"),
    (10**6, "megaohms"),
    (10**3, "kiloohms"),
    (1, "ohms"),
]

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"

    # Extraction des valeurs selon 4 ou 5 bandes
    if len(colors) == 5:
        first, second, third, multiplier = [COLORS[c] for c in colors[:4]]
        value = (first * 100 + second * 10 + third) * (10 ** multiplier)
    else:  # 4 bandes (ou par défaut)
        first, second, multiplier = [COLORS[c] for c in colors[:3]]
        value = (first * 10 + second) * (10 ** multiplier)

    tolerance = colors[-1]

    # Traitement des unités
    for factor, unit in UNITS:
        if value >= factor:
            raw_value = value / factor
            # Supprime le .0 inutile si le nombre est entier (ex: 33.0 -> 33)
            formatted_value = int(raw_value) if raw_value.is_integer() else raw_value
            return f"{formatted_value} {unit} ±{TOLERANCES[tolerance]}"

    return f"0 ohms ±{TOLERANCES[tolerance]}"