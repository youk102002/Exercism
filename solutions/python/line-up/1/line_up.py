def line_up(name, number):
    if 11 <= number % 100 <= 13:
        suffix = "th"
    else:
        suffixes = {1: "st", 2: "nd", 3: "rd"}
        suffix = suffixes.get(number % 10, "th")
        
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
    
