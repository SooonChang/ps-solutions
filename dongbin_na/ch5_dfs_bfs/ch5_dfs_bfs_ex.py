# ### 5-6
# INF = 999999999

# graph = [
#     [0, 7, 5],
#     [7, 0, INF],
#     [5, INF, 0]
# ]

# print(graph)

# ### 5-7
# graph = [[] for _ in range(3)]

# graph[0].append((1, 7))
# graph[0].append((2, 5))

# graph[1].append((0, 7))

# graph[2].append((0, 5))

# print(graph)

# ### 5-8
# ### DFS
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end = '--')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# graph = [[],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9
# dfs(graph, 1, visited)

### 5-9
### BFS
from collections import deque
import queue
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = '--')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [[],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)