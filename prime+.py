def is_prime(integer):

    i = integer - 1
    result = True

    while i > 1:
        if integer % i != 0:
            i -= 1
            continue
        
        result = False
        break
    return result

i = 2
count = 0
while i < 10000:
    if is_prime(i):
        print(i)
        count += 1
    
    i += 1

print('count is ' + str(count))