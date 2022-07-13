from collections import deque

def get_next_pos(pos, data):
    next_pos = []
    pos = list(pos)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    for i in range(4):
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]

        
        if data[nx1][ny1] == 0 and data[nx2][ny2] == 0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})
    
    if x1 == x2: # 가로로 놓여져 있을 때
        for i in [-1, 1]: # 위쪽 회전 or 아래쪽 회전
            if data[x1 + i][y1] == 0 and data[x2 + i][y2] == 0: #!!변수이름 헷갈리지 말자!!
                next_pos.append({(x1 + i, y1), (x1, y1)})
                next_pos.append({(x2 + i, y2), (x2, y2)})
    
    elif y1 == y2: # 세로로 놓여져 있을 때
        for i in [-1, 1]: # 왼쪽 회전 or 오른쪽 회전
            if data[x1][y1 + i] == 0 and data[x2][y2 + i] == 0:
                next_pos.append({(x1, y1 + i), (x1, y1)})
                next_pos.append({(x2, y2 + i), (x2, y2)})

    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    
    # 집합을 사용하는 이유 -> 배열 순서에 상관 없게 하려고!
    init_pos = {(1, 1), (1, 2)}
    q = deque()
    q.append((init_pos, 0))
    
    visited = []
    visited.append(init_pos)

    while q:
        pos, val = q.popleft()

        if (n, n) in pos:
            return val
        
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, val + 1))
                visited.append(next_pos)
    return 0
