def cal(a, b, operator):
    return a + b if operator == '+' else a - b if operator == '-' else a * b if operator == '*' else a / b if operator == '/' else 'error'

print(cal(1, 5, '/'))