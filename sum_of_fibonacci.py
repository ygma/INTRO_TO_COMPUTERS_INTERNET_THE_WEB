def cal_sum_fibo(n):
    a, b = 1, 1
    sum = a + b
    for i in range(3, n + 1):
        c = a + b
        sum += c
        a, b = b,c
        
    return sum

print(cal_sum_fibo(8))
