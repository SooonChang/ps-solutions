# import copy
# T = int(input())
# INF = int(1e9)

# result = []
# delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# for _ in range(T):
#     n = int(input())
#     data = []

#     for _ in range(n):
#         arr = list(map(int, input().split()))
#         data.append(arr)
    
#     dp = [[INF] * n for _ in range(n)]

#     dp[0][0] = data[0][0]
    
#     # 플로이드
#     for r in range(n):
#         for c in range(n):
#             for dx, dy in delta:
#                 nx = r + dx
#                 ny = c + dy

#                 if 0<= nx < n and 0 <= ny <n:
#                     dp[r][c] = min(dp[r][c], dp[nx][ny] + data[r][c])

#     result.append(dp[n -1][n - 1])

# for i in result:
#     print(i)

# ### db_na
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
result = []
for _ in range(T):
    n = int(input())

    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    
    distance = [[INF] * n for _ in range(n)]
    q = []
    x, y = 0, 0
    distance[x][y] = data[x][y]
    heapq.heappush(q, (data[x][y], x, y))

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어날 때 예외처리
            if nx < 0 or nx >=n or ny <0 or ny >=n:
                continue
            
            cost = dist + data[nx][ny]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    result.append(distance[n-1][n-1])

for i in result:
    print(i)
    

