import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
exist_shark = list(i for i in range(1, m + 1)) # 남아있는 상어 리스트
res = 0

class Shark:
    def __init__(self, x, y, i):
        self.idx = i
        self.is_exist = True
        self.x = x
        self.y = y
        self.cur_dir = -1
        self.dir = [[] for _ in range(4)]
    
    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_dir(self, direction):
        self.cur_dir = direction
    
    def set_dir_matrix(self, directions, idx):
        self.dir[idx] = directions
    
    def cur_pos(self):
        return (self.x , self.y, self.cur_dir)
    
    def cur_state(self):
        return self.is_exist
    
    def cur_direction(self, d):
        return self.dir[d]
    
    def remove(self):
        self.is_exist = False

sh_list = [None] * (m + 1) # 상어 객체들
array = [[None] * n for _ in range(n)] # 맵

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 위, 아래, 왼쪽, 오른쪽


for x in range(n):
    data = list(map(int, input().split()))
    for y in range(n):
        if data[y] == 0:
            array[x][y] = [0, 0]
        else:
            sh_list[data[y]] = Shark(x, y, data[y])
            array[x][y] = [data[y], k]

data = list(map(int, input().split()))
for i in range(m):
    sh_list[i + 1].set_dir(data[i] - 1)

for i in range(m):
    for j in range(4):
        data = list(map(int, input().split()))
        for d in range(4):
            data[d] -= 1
        sh_list[i + 1].set_dir_matrix(data, j)

def next_move():
    move_list = []

    for i in range(1, m + 1):
        if not sh_list[i].cur_state():
            continue

        cx, cy, cd = sh_list[i].cur_pos()
        direction = sh_list[i].cur_direction(cd)

        next_x, next_y, next_d = -1, -1, -1
        found = False
        for d in direction: # 우선순위에 따라 빈공간 찾기
            nx, ny = cx + delta[d][0], cy + delta[d][1]

            if 0 <= nx < n and 0 <= ny < n:
                if array[nx][ny][0] == 0:
                    next_x, next_y, next_d = nx, ny, d
                    found = True
                    break
        
        if not found: # 빈공간이 없는 경우
            for d in direction:
                nx, ny = cx + delta[d][0], cy + delta[d][1]
                if 0 <= nx < n and 0 <= ny < n:
                    if array[nx][ny][0] == i:
                        next_x, next_y, next_d = nx, ny, d
                        found = True
                        break
        
        if (next_x, next_y) not in move_list:
            move_list.append((next_x, next_y))
            sh_list[i].set_pos(next_x, next_y)
            sh_list[i].set_dir(next_d)
        
        else:
            sh_list[i].remove()
            exist_shark.remove(i)

def make_step():
    
    next_move()

    # 냄새 1씩 제거
    for x in range(n):
        for y in range(n):
            if array[x][y][0] != 0:
                array[x][y][1] -= 1

            if array[x][y][1] == 0:
                    array[x][y][0] = 0
    
    # 현재 상어 위치 냄새 추가
    for i in range(1, m + 1):
        if not sh_list[i].cur_state():
            continue

        cx, cy, cd = sh_list[i].cur_pos()
        array[cx][cy][0] = i
        array[cx][cy][1] = k

while len(exist_shark) > 1 and res <= 1000:
    make_step()
    res += 1

if res > 1000:
    print(-1)
else:
    print(res)