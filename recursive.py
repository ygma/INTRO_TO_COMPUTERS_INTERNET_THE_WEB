#def fibo(n):
#    if n == 1 or n == 2:
#        return 1
#    
#    return fibo(n - 1) + fibo(n - 2)
#
#for i in range (1, 10):
#    print(fibo(i), end = ' ')
    
#def sum_fibo(n):
#    if n == 1:
#        return 1
#    return fibo(n) + sum_fibo(n - 1)
#
#print(sum_fibo(5))

def search(list, TargetValue):
    if not list:
        return 'failed'
    else:
        i = round(len(list) / 2)
        TestEntry = list[i]
        if TargetValue == TestEntry:
            return 'succeeded'
        if TargetValue < TestEntry:
            return search(list[:i], TargetValue)
        if TargetValue > TestEntry:
            return search(list[i + 1:], TargetValue)
    

print(search(['a', 'b', 'c', 'd', 'e'], 'gjj'))
list = [1, 2, 3, 4, 5]