def is_prime(integer):
    for i in range(2, integer):
        if integer % i == 0:
            return False
    return True

def get_primes_between(a, b):
    result = []
    for i in range(a, b + 1):
        if is_prime(i):
#            result.append(i)
            result += [i]
    
    return result

print(get_primes_between(5, 19))
