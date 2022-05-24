### 5-10
n, m = map(int,input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))

def dfs(x, y, n, m, graph):
    if x <= -1 or x >= m or y <= -1 or y>= n:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(x, y-1, n, m, graph)
        dfs(x - 1 , y, n, m, graph)
        dfs(x + 1, y, n, m, graph)
        dfs(x, y + 1, n, m, graph)
        return True
    return False

graph_ = []
for i in range(n):
    graph_.append(list(map(int,input())))

result = 0
for i in range(m):
    for j in range(n):
        if dfs(i, j, n, m, graph_):
            result +=1
print(result)