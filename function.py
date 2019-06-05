import math

sideA = int(input('side A is ?'))
sideB = int(input('side B is ?'))

result = math.sqrt(sideA**2 + sideB**2)
result = int(result)
print('result is ' + str(result))