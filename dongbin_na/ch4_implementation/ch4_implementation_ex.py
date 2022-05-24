import time

### 4-1
#####################
# n = int(input())
# route = list(map(ord, input().split()))
# start = time.time()
# cur_point = [1, 1]
# tmp_point = cur_point.copy()

# for i in route:
#     if chr(i) == 'L':
#         cur_point[1] -=1
#     elif chr(i) == 'R':
#         cur_point[1] +=1
#     elif chr(i) == 'U':
#         cur_point[0] -=1
#     elif chr(i) == 'D':
#         cur_point[0] +=1
#     else:
#         continue

#     if cur_point[0] <1 or cur_point[0] > n:
#         cur_point = tmp_point.copy()
#     elif cur_point[1] <1 or cur_point[1] > n:
#         cur_point = tmp_point.copy()
#     else:
#         tmp_point = cur_point.copy()

# print(cur_point[0], cur_point[1])
# print(time.time() - start)
##################################
# n = int(input())
# x, y = 1, 1
# plans = input().split()

# start = time.time()
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny

# print(x,y)
# print(time.time()-start)
##################################

### 4-2
# 0~59까지 3이 포함되는 경우
# 10 + 5
# h = int(input())
# count = 0
# for i in range(h + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count+=1
# print(count)

### 4-2
# n = input()

# hor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# ver = [1, 2, 3, 4, 5, 6, 7, 8]
# x, y = 0, 0
# cnt = 0
# for i in range(8):
#     for j in range(8):
#         pnt = hor[i] + str(ver[j])
#         if pnt == n:
#             x = i+1
#             y = j+1
#             break
# dx = [2, 2, -2, -2, 1, -1, 1, -1]
# dy = [1, -1, 1, -1, 2, 2, -2, -2]

# for i in range(8):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if nx < 1 or nx > 8 or ny < 1 or ny > 8:
#         continue
#     cnt +=1
# print(cnt)
############################################
# input_data = input()
# row = int(input_data[1])
# col = int(ord(input_data[0]) - ord('a')) + 1

# steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
# cnt = 0
# for i in steps:
#     nx = row + i[0]
#     ny = row + i[1]
#     if 1<= nx <=8 and 1<=ny<=8:
#         cnt+=1

# print(cnt)
###########################################

### 4-3
# # N : 0, E : 1, S : 2, W : 3
########################
# n, m = map(int, input().split())
# x, y, direction = map(int, input().split())

# d = [[0] * m for _ in range(n)]
# d[x][y] = 1

# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3

# count = 1
# turn_time = 0
# while True:
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]

#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     else:
#         turn_time += 1
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         else:
#             break
#         turn_time = 0
# print(count)