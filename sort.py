def sort1(list):
    n = 1
    while n < len(list):
        pivot = list[n]
        list[n] = None
        
        m = n - 1
        hole_index = n
        while m >= 0:
            if list[m] > pivot:
                list[m + 1], list[m] = list[m], list[m + 1]
                hole_index = m
            m -= 1
        
        list[hole_index] = pivot
        n += 1
        
    return list

def sort2(list):
    is_done = False
    while not is_done:
        is_done = True
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                is_done = False
    return list

print(sort1(['delta', 'alfa', 'bravo', 'echo', 'charlie']))
print(sort1([5, 3, 4, 1, 2]))

print(sort2(['delta', 'alfa', 'bravo', 'echo', 'charlie']))