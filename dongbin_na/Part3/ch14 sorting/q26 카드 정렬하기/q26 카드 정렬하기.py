import heapq

n = int(input())
data = []
for _ in range(n):
    heapq.heappush(data, int(input()))

total_sum = 0
while True:
    first = heapq.heappop(data)
    if not data:
        break
    
    second = heapq.heappop(data)

    total_sum += (first + second)
    heapq.heappush(data, (first + second))

print(total_sum)