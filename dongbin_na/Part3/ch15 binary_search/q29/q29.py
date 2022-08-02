### https://www.acmicpc.net/problem/2110
n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort()
start = 1
end = array[-1] - array[0]
result = 0

while end >= start:
    gap = (start + end) // 2

    value = array[0]
    cnt = 1

    for i in range(1, n):
        if array[i] - value >= gap:
            value = array[i]
            cnt += 1
    
    if cnt >= c:
        start = gap + 1
        result = gap
    else:
        end = gap - 1

print(result)