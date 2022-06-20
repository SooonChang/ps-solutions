from itertools import combinations

n = int(input())
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]

board = []
teacher = []
student = []
candidates = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'S':
            student.append((i, j))
        elif board[i][j] == 'T':
            teacher.append((i, j))
        else:
            candidates.append((i, j))


def check_proper(x, y):
    
    proper = True
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy

        while 0<= nx < n and 0<= ny < n:
            if board[nx][ny] == 'O':
                break
            elif board[nx][ny] == 'S':
                
                return False
            else:
                nx += dx
                ny += dy
    return proper

answer = False
for candidate in list(combinations(candidates, 3)):
    for cx, cy in candidate:
        board[cx][cy] = 'O'
    
    answer = True
    for tx, ty in teacher:
        if check_proper(tx, ty) == False:
            answer = False
            break
    if answer == True:
        break
    for cx, cy in candidate:
        board[cx][cy] = 'X'

if answer == False:
    print("NO")
else:
    print("YES")
