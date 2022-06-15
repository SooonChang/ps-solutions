### https://www.acmicpc.net/problem/15686
### 첫번째 풀이
# from itertools import combinations
# def distance(x1, y1, x2, y2):
#     return abs(x1 - x2) + abs(y1 - y2)

# n, m = map(int, input().split())
# INF = int(1e9)
# chicken = []
# home = []

# for i in range(n):
#     buffer = list(map(int, input().split()))

#     for j in range(n):
#         if buffer[j] == 1:
#             home.append((i,j))
#         elif buffer[j] == 2:
#             chicken.append((i,j))

# dist_matrix = [[0] * len(chicken) for _ in range(len(home))]

# for i in range(len(home)):
#     for j in range(len(chicken)):
#         dist = distance(home[i][0], home[i][1], chicken[j][0], chicken[j][1])
#         dist_matrix[i][j] = dist
# chicken_idx = []
# for i in range(len(chicken)):
#     chicken_idx.append(i)

# candidates = list(combinations(chicken_idx, m))

# result = INF
# for candidate in candidates:
#     buffer = 0
#     for h in range(len(home)):
#         min_val = INF
#         for c in candidate:
#             if min_val > dist_matrix[h][c]:
#                 min_val = dist_matrix[h][c]
#         buffer += min_val
#     if buffer < result:
#         result = buffer

# print(result)

### 동빈나
from itertools import combinations

n, m = map(int,input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반 집
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨 집

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        temp = int(1e9)
        for cx, cy in candidate:
             temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = int(1e9)
for candidate in candidates:
    result = min(result, get_sum(candidate))
print(result)
