def get_multiplication():
    result = []
    for i in range(1, 10):
        line = []
        
        for j in range(1, 10): line.append(i * j)
            
        result.append(line)
    
    return result
    
for i in get_multiplication():
    print(i)
