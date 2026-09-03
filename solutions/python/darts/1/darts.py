
def score(x, y):
    result = x**2 + y**2
    if result <= 1 :
        return 10
    if result <= 25 :
        return 5
    if result <= 100 :
        return 1
    return 0
        
    
        
