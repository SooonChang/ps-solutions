from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
graph = []

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class shark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.big = 2
        self.ate = 0
    
    def cur_pos(self):
        return (self.x, self.y)
    
    def cur_size(self):
        return self.big
    
    def check_cur_state(self):
        if self.big == self.ate:
            self.big += 1
            self.ate = 0

    def eat_fish(self, x, y):
        self.x = x
        self.y = y
        self.ate += 1

        self.check_cur_state()

for x in range(N): # map 정보 받기
    graph.append(list(map(int, input().split())))

for x in range(N): # 상어 위치 찾기
    for y in range(N):
        if graph[x][y] == 9:
            sh = shark(x, y)
            graph[x][y] = 0

def bfs():
    dist = [[-1] * N for _ in range(N)]
    q = deque()

    x, y = sh.cur_pos()
    dist[x][y] = 0
    q.append((x, y, 0))

    while q:
        cx, cy, d = q.popleft()

        for dx, dy in delta:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < N and 0 <= ny < N: # 맵 범위 벗어나는 경우제외
                if dist[nx][ny] == -1 and graph[nx][ny] <= sh.cur_size():
                    dist[nx][ny] = d + 1
                    q.append((nx, ny, d + 1))

    return dist

def find_next(dist):

    min_dist = INF
    min_x = INF
    min_y = INF
    
    for x in range(N):
        for y in range(N):

            if 0 < dist[x][y] < min_dist:
                if 0 < graph[x][y] < sh.cur_size():
                    min_x = x
                    min_y = y
                    min_dist = dist[x][y]
            
            elif dist[x][y] == min_dist:
                if 0 < graph[x][y] < sh.cur_size():
                    if x < min_x:
                        min_x = x
                        min_y = y
        
    return min_x, min_y, min_dist

cnt = 0

while True:
    dist = bfs()
    x, y, d = find_next(dist)

    if d == INF:
        break

    sh.eat_fish(x, y)
    cnt += d
    graph[x][y] = 0

print(cnt)