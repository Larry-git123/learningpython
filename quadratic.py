import math

def quadratic(a, b, c):
    if a == 0:
        if b == 0:
            root = ()
        else:
            root = (-c / b,)
    else:
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            root = ((-b + math.sqrt(discriminant)) / (2 * a), (-b - math.sqrt(discriminant)) / (2 * a))
        elif discriminant == 0:
            root = (-b / (2 * a),)
        else:
            root = ()
    return root