import sys
import copy

input = sys.stdin.readline

res = 0
fishes = [[] for _ in range(17)] # (d, x, y) 방향, x, y
fishes[0] = (-1, -1, -1)
graph = []
delta =[(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

for x in range(4):
    buffer = list(map(int, input().split()))
    graph.append(buffer[0:8:2])

    for y in range(4):
        fishes[buffer[2 * y]] = ((buffer[2*y + 1], x, y))


def is_movable(graph, x, y):

    if 0 <= x < 4 and 0 <= y < 4:
        if graph[x][y] != -1:
            return True
        else:
            return False
    else:
        return False

def make_move(fishes, graph):

    for i in range(1, 17):
        d, x, y = fishes[i]
        if d == -1:
            continue

        while is_movable(graph, x + delta[d - 1][0], y + delta[d - 1][1]) == False:
            d = d % 8 + 1
        
        nx = x + delta[d - 1][0]
        ny = y + delta[d - 1][1]
        c_idx = graph[nx][ny]
        if c_idx >= 1 and fishes[c_idx][0] != -1:
            fishes[i], fishes[c_idx] = (d, nx, ny), (fishes[c_idx][0], x, y)
            graph[nx][ny], graph[x][y] = i, c_idx
        else:
            fishes[i] = (d, nx, ny)
            graph[nx][ny], graph[x][y] = i, 0

def find_available_path(graph, x, y, d):
    dx, dy = delta[d - 1]
    nx = x + dx
    ny = y + dy
    candidate = []

    while 0<= nx < 4 and 0<= ny < 4:
        if graph[nx][ny] > 0:
            candidate.append((nx, ny))
        nx += dx
        ny += dy

    return candidate



def dfs(graph, fishes, x, y, total):

    global res
    graph = copy.deepcopy(graph)
    fishes = copy.deepcopy(fishes)

    d = fishes[graph[x][y]][0]
    total += graph[x][y]
    res = max(res, total)
    fishes[graph[x][y]] = (-1, -1, -1)
    graph[x][y] = -1

    make_move(fishes, graph)
    candidate = find_available_path(graph, x, y, d)
    graph[x][y] = 0
    
    if not candidate:
        return
    else:
        for nx, ny in candidate:
            dfs(graph, fishes, nx, ny, total)


dfs(graph, fishes, 0, 0, 0)
print(res)