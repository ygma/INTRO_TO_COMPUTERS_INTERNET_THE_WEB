def get_power(n, p):
    result = n
    for i in range(2, p + 1):
        result *= n
    return result

print(get_power(5, 3))