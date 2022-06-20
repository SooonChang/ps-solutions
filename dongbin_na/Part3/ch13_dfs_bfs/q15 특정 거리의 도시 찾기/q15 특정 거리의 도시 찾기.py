### https://www.acmicpc.net/problem/18352
from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())

graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n + 1)
cost = [0] * (n + 1)

q = deque()
q.append(x)
visited[x] = True

while q:
    now = q.popleft()

    for i in graph[now]:
        if visited[i] == False:
            visited[i] = True
            cost[i] = cost[now] + 1
            q.append(i)

cnt = 0
for i in range(1, len(cost)):
    if cost[i] == k:
        print(i)
        cnt += 1
if cnt == 0:
    print(-1)