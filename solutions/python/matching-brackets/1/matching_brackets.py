def is_paired(input_string):
    pairs = { "{":"}","[":"]","(":")"}
    closing_brackets = set(pairs.values())    
    stack = []
    for char in input_string :         
        if char in pairs : 
            stack.append(pairs[char])             
        elif char in closing_brackets :
            if not stack or stack.pop() != char : 
                return False
    
    return not stack                