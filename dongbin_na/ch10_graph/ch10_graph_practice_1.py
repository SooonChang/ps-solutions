### 팀 결성

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

def check_parent(parent, a, b):
    if find_parent(parent, b) == find_parent(parent, a):
        print("YES")
    else:
        print("NO")

n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

oper_list = []
for i in range(m):
    buffer = list(map(int, input().split()))
    oper_list.append(buffer)

for i in oper_list:
    if i[0] == 0:
        union(parent, i[1], i[2])
    elif i[0] == 1:
        check_parent(parent, i[1], i[2])
