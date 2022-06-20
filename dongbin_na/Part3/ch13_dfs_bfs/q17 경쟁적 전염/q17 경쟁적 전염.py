### https://www.acmicpc.net/problem/18405
# import sys
# input = sys.stdin.readline
# from collections import deque

# n, k = map(int, input().split())
# data = [] # 전체 보드
# vir = [deque() for _ in range(k + 1)] # 바이러스 정보를 담는 que

# for r in range(n):
#     tmp = list(map(int, input().split()))
#     for c in range(n):
#         if tmp[c] != 0: # 바이러스가 있으면
#             vir[tmp[c]].append((r, c)) # 해당 좌표를 해당 바이러스 que 에 append
#     data.append(tmp)

# s, tx, ty = map(int, input().split())

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# def virus_propagation(v, x, y):
#     if x < 0 or x >= n or y < 0 or y >= n:
#         return False
#     elif data[x][y] != 0:
#         return False
#     else:
#         data[x][y] = v
#         return True

# for sec in range(s): # target s동안
#     for v in range(1, k + 1): # 바이러스 인덱스 낮은 순부터
#         buffer = []
#         while vir[v]: # 현재 시간에 담겨있는 바이러스 정보 모두 비움
#             buffer.append(vir[v].popleft())
#         for x, y in buffer:
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if virus_propagation(v, nx, ny):
#                     vir[v].append((nx, ny))

# print(data[tx-1][ty-1])

### 동빈나 풀이
from collections import deque

n, k = map(int, input().split())
graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] !=0:
            # (바이러스 종류, 시간, 위치 x, 위치 y) 삽임
            data.append((graph[i][j], 0, i, j))

# 낮은 바이러스 순으로 정렬
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])