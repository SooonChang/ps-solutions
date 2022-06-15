### 커리큘럼
from collections import deque
import copy

def topology_sort(graph, indegree, cost):
    q = deque()
    result_ = copy.deepcopy(cost)
    
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now_ = q.popleft()

        for i in graph[now_]:
            indegree[i] -= 1
            result_[i] = max(result_[i], result_[now_] + cost[i])
            if indegree[i] == 0:
                q.append(i)
    
    return result_

n = int(input())

graph = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)
cost = [0] * (n + 1)

for i in range(1, n + 1):
    course = list(map(int, input().split()))
    cost[i] = course[0]
    for j in course[1:]:
        if j == -1:
            continue
        graph[j].append(i)
        indegree[i] += 1

result_ = topology_sort(graph, indegree, cost)
for i in range(1, len(result_)):
    print(result_[i])