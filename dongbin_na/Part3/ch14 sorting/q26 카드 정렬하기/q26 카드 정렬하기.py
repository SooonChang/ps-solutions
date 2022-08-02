import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

heapq.heapify(data)
total_sum = 0
while True:
    first = heapq.heappop(data)
    if not data:
        break
    
    second = heapq.heappop(data)

    total_sum += (first + second)
    heapq.heappush(data, (first + second))

print(total_sum)