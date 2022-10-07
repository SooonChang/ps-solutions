import heapq
INF = int(1e9)
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance[1] = 0
# 최단 거리 정보를 담을 리스트 선언
q = []
heapq.heappush(q, (0, 1))

# 다익스트라
while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

max_dist = max(distance[1:])
result = []
for i in range(1, n + 1):
    if distance[i] == max_dist:
        result.append(i)

print(result[0], max_dist, len(result))
print(distance)