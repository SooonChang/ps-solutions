### 도시 분할 계획
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parents = [0] * (n + 1)
for i in range(n + 1):
    parents[i] = i

village_list = []
for i in range(m):
    a, b, cost = map(int, input().split())
    village_list.append((cost, a, b))

village_list.sort()
res , last = 0, 0

for i in village_list:
    cost, a, b = i
    if find_parent(parents, a) != find_parent(parents, b):
        union(parents, a, b)
        res += cost
        last = cost

print(res - last)