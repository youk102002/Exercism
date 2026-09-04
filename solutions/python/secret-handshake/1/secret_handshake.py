ACTIONS = [
    (0b00001, "wink"),
    (0b00010, "double blink"),
    (0b00100, "close your eyes"),
    (0b01000, "jump")
]

def commands(binary_str):
    code = int(binary_str, 2)
    actions =[]

    for mask, action in ACTIONS :
        if code & mask :
            actions.append(action)
    if code & 0b10000 :
        actions.reverse()
    return actions
