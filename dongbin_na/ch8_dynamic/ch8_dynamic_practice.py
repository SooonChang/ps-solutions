### 8-2
# n = int(input())

# d = [0] * 30001
# for i in range(2, n+1):
#     d[i] = d[i -1 ] + 1
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)

# print(d[n])

### 8-3
# n = int(input())
# storage = list(map(int, input().split()))
# d = [0] * 100
# d[0] = storage[0]
# d[1] = max(storage[0], storage[1])
# for i in range(2, n):
#     d[i] = max(d[i-1], d[i-2] + storage[i])

# print(d[n-1])

### 8-4
# n = int(input())
# d = [0] * 1001
# d[1] = 1
# d[2] = 3

# for i in range(3, n+1):
#     d[i] = (d[i-1] + d[i-2] * 2) % 796796

# print(d[n])

### 8-5
n, m = map(int, input().split())
money = []

for _ in range(n):
    money.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(money[i], m + 1):
        d[j] = min(d[j], d[j-money[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])