def equilateral(sides):
    if (0 in sides):
        return False

    a, b , c = sides[0], sides[1], sides[2]
    if a == b == c :
        return True
    return False

def isosceles(sides):
    if (0 in sides):
        return False

    a, b , c = sides[0], sides[1], sides[2]
    if a <= b + c and b <= a + c and c <= a + b :
        if a == b == c :
            return True
        if (a == b != c) or (a == c != b) or (b == c != a) :
            return True
    return False

def scalene(sides):
    if (0 in sides):
        return False

    a, b , c = sides[0], sides[1], sides[2]
    if a <= b + c and b <= a + c and c <= a + b :
        if a != b and a != c and b != c :
            return True
    return False
