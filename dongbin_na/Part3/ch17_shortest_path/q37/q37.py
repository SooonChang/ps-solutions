import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 그래프 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 버스 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 에서 b로 가는 경로 중 비용이 작은 경로를 선택
    graph[a][b] = min(graph[a][b], c)

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행한 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 0 이라고 출력
        if graph[a][b] == INF:
            print(0, end = " ")
        else:
            print(graph[a][b], end = " ")
    print()
