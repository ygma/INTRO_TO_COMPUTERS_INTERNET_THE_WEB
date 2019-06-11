def get_all_divisors(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0: result += [i]
        
    return result

number = int(input('Please input a number: '))
divisors = get_all_divisors(number)
print(divisors)