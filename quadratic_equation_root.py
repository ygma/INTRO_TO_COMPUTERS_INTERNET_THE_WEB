import math

def cal_quadratic_equation_root(a, b, c):
    result1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    result2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return (result1, result2)

print(cal_quadratic_equation_root(1, -3, 2))