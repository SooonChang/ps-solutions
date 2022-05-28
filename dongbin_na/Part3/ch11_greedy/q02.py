array = list(map(int, input()))

result = int(array[0])

for i in range(1, len(array)):
    if array[i] <= 1 or result <=1:
        result += array[i]
    
    else:
        result *= array[i]

print(result)