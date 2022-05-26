# ### 5-3
# n, m = map(int,input().split())

# # graph = []
# # for i in range(n):
# #     graph.append(list(map(int,input())))

# def dfs(x, y, n, m, graph):
#     if x <= -1 or x >= m or y <= -1 or y>= n:
#         return False
#     if graph[y][x] == 0:
#         graph[y][x] = 1
#         dfs(x, y-1, n, m, graph)
#         dfs(x - 1 , y, n, m, graph)
#         dfs(x + 1, y, n, m, graph)
#         dfs(x, y + 1, n, m, graph)
#         return True
#     return False

# graph_ = []
# for i in range(n):
#     graph_.append(list(map(int,input())))

# result = 0
# for i in range(m):
#     for j in range(n):
#         if dfs(i, j, n, m, graph_):
#             result +=1
# print(result)

### 5-4
from collections import deque
import queue
n, m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append([0,0])
while queue:
    pnt = queue.popleft()
    for i in range(4):
        x , y = pnt[0], pnt[1]
        dist = graph[y][x]
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <=-1 or nx >= m or ny<=-1 or ny>=n:
            continue
        if  graph[ny][nx] == 1:
            queue.append([nx, ny])
            graph[ny][nx] += dist

print(graph[n-1][m-1])
print(graph)