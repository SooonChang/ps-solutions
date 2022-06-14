### 프림 알고리즘
import heapq
v, e = map(int, input().split())
visited = [False] * (v + 1)

edges = []
result = 0

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    heapq.heappush(edges, (cost, a, b))

### 나중에...
