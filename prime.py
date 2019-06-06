input_number = int(input('please input a number: '))

i = input_number - 1
is_prime = True

while i > 1:
    if input_number % i != 0:
        i -= 1
        continue
    
    is_prime = False
    break

if is_prime:
    print('is prime')
else:
    print('is not prime')
