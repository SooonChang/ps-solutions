### https://www.acmicpc.net/problem/14502
from itertools import combinations
import copy

n, m = map(int, input().split())
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
buffer = [[0] * m for _ in range(n)]

lab = []
vir = []
candidates = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        if data[j] == 2:
            vir.append((i, j))
        elif data[j] == 0:
            candidates.append((i, j))
    lab.append(data)

result = -1

def dfs(x, y):
    if x <0 or y < 0 or x >= n or y >= m:
        return
    if buffer[x][y] == 0:
        buffer[x][y] = 2

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            dfs(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if buffer[i][j] == 0:
                score += 1
    return score

def get_result(candidates, vir):
    global result
    for candidate in list(combinations(candidates, 3)):
        for i in range(n):
            for j in range(m):
                buffer[i][j] = lab[i][j]
        for x, y in candidate:
            buffer[x][y] = 1
        
        for x, y in vir:
            for dx, dy in delta:
                dfs(x + dx, y + dy)
        
        score = get_score()
        
        result = max(result, score)

get_result(candidates, vir)
print(result)

### 동빈나 
# n, m = map(int, input().split())
# data = [] # 초기 맵 리스트
# temp = [[0] * m for _ in range(n)]

# for _ in range(n):
#     data.append(list(map(int, input().split())))

# # 4가지 이동 방향
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# result = 0

# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0<= nx < n and 0<= ny < m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx, ny)

# def get_score():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#     return score

# # DFS를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
# def dfs(count):
#     global result
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = data[i][j]
#         # 바이러스의 위치에서 전파 진행
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i, j)
#         # 안전 영역의 최댓값 계산
#         result = max(result, get_score())
#         return
#     # 빈 공간에 울타리 설치
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 data[i][j] = 0
#                 count -= 1
# dfs(0)
# print(result)

### 두번째 시도
# n, m = map(int, input().split())
# lab = []
# vir = []
# candidates = []

# for i in range(n):
#     data = list(map(int, input().split()))
#     for j in range(m):
#         if data[j] == 2:
#             vir.append((i, j))
#         elif data[j] == 0:
#     lab.append(data)

