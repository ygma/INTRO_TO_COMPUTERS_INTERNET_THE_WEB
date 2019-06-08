def cal_greatest_common_divisor(a, b):
    a = max(a, b)
    b = min(a, b)
    reminder = a % b
    return b if reminder == 0 else cal_greatest_common_divisor(b, reminder)

print(cal_greatest_common_divisor(78, 66))


