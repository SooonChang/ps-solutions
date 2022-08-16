delta = [(0, 1), (1, 1), (-1, 1)]

def get_result(array, n, m):
    cost = [[0] * m for _ in range(n)]
    max_val = 0
    for i in range(n):
        cost[i][0] = array[i * m]

    for y in range(1, m):
        for x in range(n):
            for dx, dy in delta:
                px, py = x - dx, y - dy
                
                if px < 0 or px >= n:
                    continue
                cost[x][y] = max(cost[x][y], cost[px][py] + array[m * x + y])
            if y == m - 1:
                max_val = max(max_val, cost[x][y])
    return max_val

result = []
T  = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result.append(get_result(data, n, m))

for res in result:
    print(res)