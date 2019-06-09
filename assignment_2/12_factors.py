def cal_factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0: result.append(i)
        
    return result

print(cal_factors(10))