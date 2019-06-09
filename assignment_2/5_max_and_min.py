import sys

def get_max_and_min(a, b, c):
#    list = [a, b, c]
#    return (min(a, b, c), max(a, b, c))
    if a < b:
        min, max = a, b
    else:
        min, max = b, a
        
    if c < min:
        min = c
    if c > max:
        max = c
        
    return (min, max)
        
    

print(get_max_and_min(3,8,2))
    