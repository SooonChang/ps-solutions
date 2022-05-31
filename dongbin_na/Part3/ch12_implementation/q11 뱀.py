from collections import deque
n = int(input())
k = int(input())
apple = []
for _ in range(k):
    y, x = map(int, input().split())
    apple.append((x, y))

l = int(input())
changes = deque()
for _ in range(l):
    x, c = input().split()
    changes.append([int(x), c])
####
delta = [(1, 0), (0, -1), (-1, 0), (0, 1)]
board = [[0] * (n + 1) for _ in range(n + 1)]
for i in apple:
    x, y = i[0], i[1]
    board[y][x] = -1
###
snake = deque()
snake.append([1, 1])
hx, hy = 1, 1
dir = 0
cnt = 0
###
change_t, change_c = changes.popleft()

while snake:
    over = False
    if cnt == change_t:
        if change_c == 'L': dir = ((dir + 4) + 1) % 4
        elif change_c == 'D': dir = ((dir + 4) - 1) % 4
        
        if changes: change_t, change_c = changes.popleft()
    
    nx, ny = hx + delta[dir][0], hy + delta[dir][1]

    if nx <= 0 or nx > n or ny <= 0 or ny >n:
        cnt +=1
        break

    for i in snake:
        if nx == i[0] and ny == i[1]:
            cnt +=1
            over = True
            break
    if over:
        break

    eaten = True
    for i in range(len(apple)):
        if nx == apple[i][0] and ny == apple[i][1]:
            apple[i], apple[-1] = apple[-1], apple[i]
            apple.pop()
            eaten = False
            break
    
    snake.append([nx, ny])
    hx = nx
    hy = ny
    if eaten:
        snake.popleft()
    cnt += 1

print(cnt)