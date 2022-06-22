# ### https://www.acmicpc.net/problem/16234
# from collections import deque
# n, l, r = map(int, input().split())

# data = []
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# for i in range(n):
#     data.append(list(map(int, input().split())))

# result = 0

# def process(x, y, idx):
#     if x < 0 or x >= n or y < 0 or y >=n:
#         return

#     union_list[x][y] = idx
#     que = deque()
#     que.append((x, y))

#     united = []
#     united.append((x, y))
#     cnt = 1
#     sum_val = data[x][y]

#     while que:
#         cx, cy = que.popleft()
#         for i in range(2):
#             nx = cx + dx[i]
#             ny = cy + dy[i]

#             if 0 <= nx < n and 0 <= ny < n:
#                 if l <= abs(data[cx][cy] - data[nx][ny]) <=r:
#                     que.append((nx, ny))
#                     union_list[nx][ny] = idx
#                     cnt += 1
#                     sum_val += data[nx][ny]
#                     united.append((nx, ny))
    
#     val = sum_val // cnt
#     for i, j in united:
#         data[i][j] = val
    
#     return cnt

# result = 0
# while True:
#     union_list = [[-1] * n for _ in range(n)]
#     index = 0
#     changed = False
#     for x in range(n):
#         for y in range(n):
#             if union_list[x][y] == -1:
#                 process(x, y, index)
#                 index += 1
#                 changed = True
    
#     if changed == False:
#         break
#     result += 1

# print(result)

### 동빈나
# from collections import deque

# n, l, r = map(int, input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# result = 0

# def process(x, y, index):
#     united = []
#     united.append((x, y))

#     q = deque()
#     q.append((x, y))
#     union[x][y] = index
#     summary = graph[x][y]
#     count = 1

#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0<= nx < n and 0 <= ny < n and union[nx][ny] == -1:
#                 if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
#                     q.append((nx, ny))
#                     union[nx][ny] = index
#                     summary += graph[nx][ny]
#                     count += 1
#                     united.append((nx, ny))

#     for i, j in united:
#         graph[i][j] = summary // count
    
#     return count

# total_count = 0

# while True:
#     union = [[-1] * n for _ in range(n)]
#     index = 0
#     for i in range(n):
#         for j in range(n):
#             if union[i][j] == -1:
#                 process(i, j, index)
#                 index += 1
#     if index == n * n:
#         break
#     total_count += 1

# print(total_count)

# ### 두 번째 풀이
# import sys
# sys.setrecursionlimit(10**9)
# n, l, r = map(int, input().split())

# data = []
# delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# for i in range(n):
#     data.append(list(map(int, input().split())))

# visited = [[False] * n for _ in range(n)]

# def dfs(x, y, buffer):
#     global S
#     if x < 0 or x >= n or y <0 or y >=n:
#         return
#     elif visited[x][y]:
#         return
    
#     buffer.append((x, y))
#     visited[x][y] = True
#     S += data[x][y]
#     for dx, dy in delta:
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#             if l <= abs(data[x][y] - data[nx][ny]) <= r:
#                 dfs(nx, ny, buffer)


# result = 0
# while True:
#     visited = [[False] * n for _ in range(n)]
#     flag = False

#     stack = []
#     for x in range(n):
#         for y in range(n):
#             if not visited[x][y]:
#                 buffer = []
#                 S = 0
#                 dfs(x, y, buffer)
#                 if len(buffer) == 1:
#                     continue
#                 stack.append([S // len(buffer), buffer])

#     for tar, tmp in stack:
#         for r, c in tmp:
#             data[r][c] = tar
#         if len(tmp) > 1:
#             flag = True

#     if flag:
#         result += 1
#     else:
#         break
# print(result)

### 다른사람 풀이 참고
from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
data =[]
for _ in range(n):
    data.append(list(map(int, input().split())))
visited = [[-1 for _ in range(n)] for _ in range(n)]

search = deque()
for i in range(n):
    for j in range(n):
        search.append((i, j))

def process(x, y, idx):
    q = deque()
    q.append((x, y))
    union = [(x, y)]
    sum_val = data[x][y]
    visited[x][y] = idx

    while q:
        cx, cy = q.popleft()
        for dx, dy in delta:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] != idx and l <= abs(data[cx][cy] - data[nx][ny]) <= r:
                    sum_val += data[nx][ny]
                    q.append((nx, ny))
                    visited[nx][ny] = idx
                    union.append((nx, ny))
    if len(union) > 1:
        average = sum_val // len(union)
        for tx, ty in union:
            data[tx][ty] = average
            search.append((tx, ty))
        return 1
    return 0

t = 0
while True:
    cnt = 0
    for _ in range(len(search)):
        x, y = search.popleft()
        if visited[x][y] != t:
            tmp = process(x, y, t)
            cnt += tmp
    if cnt == 0:
        break
    t += 1

print(t)
