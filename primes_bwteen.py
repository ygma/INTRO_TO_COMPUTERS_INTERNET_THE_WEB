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

def get_primes_between(a, b):
    result = []
    for i in range(a, b + 1):
        if is_prime(i):
            result.append(i)
    
    return result

print(get_primes_between(5, 19))
    