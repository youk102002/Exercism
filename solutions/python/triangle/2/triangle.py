"""Determine if a triangle is equilateral, isosceles, or scalene"""
def equilateral(sides):
    """
    Function equilateral(sides)

    Parameters:
        sides : an array with the values float or int of each side of the triangle

    Return :
        bool True if the 3 sides have same length
    
    """
    if (0 in sides):
        return False

    a, b , c = sides[0], sides[1], sides[2]
    if a == b == c :
        return True
    return False

def isosceles(sides):
    """
    Function isocseles(sides)

    Parameters:
        sides : an array with the values float or int of each side of the triangle

    Return :
        bool True if the 2 sides have same length
    
    Must repect Triangle Inequality rules :
        a + b ≥ c
        b + c ≥ a
        a + c ≥ b
    """
    if (0 in sides):
        return False

    side_a, side_b , side_c = sides[0], sides[1], sides[2]
    if side_a <= side_b + side_c and side_b <= side_a + side_c and side_c <= side_a + side_b :
        if side_a == side_b == side_c :
            return True
        if (side_a == side_b != side_c) or (side_a == side_c != side_b) or (side_b == side_c != side_a) :
            return True
    return False

def scalene(sides):
    """
    Function isocseles(sides)

    Parameters:
        sides : an array with the values float or int of each side of the triangle

    Return :
        bool True if the 2 sides have same length
    
    Must repect Triangle Inequality rules :
        a + b ≥ c
        b + c ≥ a
        a + c ≥ b
    """
    if (0 in sides):
        return False

    side_a, side_b , side_c = sides[0], sides[1], sides[2]
    if side_a <= side_b + side_c and side_b <= side_a + side_c and side_c <= side_a + side_b :
        if side_a != side_b and side_a != side_c and side_b != side_c :
            return True
    return False
