def is_prime(integer):

    i = integer - 1

    while i > 1:
        if integer % i != 0:
            i -= 1
            continue
        
        return False
        break
    return True

item1 = 1
item2 = 1
print(item1)
print(item2)

#i = 3
#while i <= 100:
while True:
    nextItem = item1 + item2
    
    if nextItem > 1000:
        break
    
    if is_prime(nextItem):
        print(nextItem)
    item1 = item2
    item2 = nextItem

#    i += 1