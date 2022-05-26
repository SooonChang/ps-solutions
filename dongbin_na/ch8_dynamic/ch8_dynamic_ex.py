### fibonacci
n = int(input())
### 8-1
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)
### 8-2
d = [0] * 100
def fibo_caching(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo_caching(x-1) + fibo_caching(x-2)
    return d[x]

print(fibo_caching(n))