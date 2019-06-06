option = int(input('Select an Option (1 for sum, 2 for production):'))
n = int(input('Input n:'))

if option == 1:
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print('Sum: ' + str(sum))

if option == 2:
    production = 1
    for i in range(1, n + 1):
        production *= i
    print('Production: ' + str(production))
        
    