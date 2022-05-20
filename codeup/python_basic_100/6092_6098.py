# ### 6092
# n = int(input())
# att_list = list(map(int, input().split()))
# if len(att_list)!=n:
#     exit()
# std_list = [0] * 23
# for i in att_list:
#     if i<=0 or i>23:
#         exit()
#     std_list[i-1] +=1

# for i in std_list:
#     print(i, end=' ')

# ### 6093
# n = int(input())
# att_list = list(map(int, input().split()))
# if(len(att_list)!=n):
#     exit()
# for i in reversed(att_list):
#     print(i, end=' ')

# ### 6094
# n = int(input())
# att_list = list(map(int, input().split()))

# if len(att_list)!=n:
#     exit()

# res = att_list[0]

# for i in att_list:
#     res = min(res, i)
# print(res)

# ### 6095
# # *** 2차원 배열
# board = [[0] * 19 for _ in range(19)]
# n = int(input())
# for _ in range(n):
#     i, j = input().split()
#     board[int(i)-1][int(j)-1] = 1

# for i in range(19):
#     for j in range(19):
#         if j==18:
#             print(board[i][j])
#         else:
#             print(board[i][j], end = ' ')

# ### 6096
# board = [[0] * 19 for _ in range(19)]
# for i in range(19):
#     board[i] = list(map(int, input().split()))
#     if len(board[i]) != 19:
#         exit()
# n = int(input())

# for _ in range(n):
#     x, y = input().split()
#     x = int(x) -1
#     y = int(y) -1
#     for i in range(19):
#         if board[i][y] == 0:
#             board[i][y] = 1
#         else:
#             board[i][y] = 0
        
#         if board[x][i] == 0:
#             board[x][i] = 1
#         else:
#             board[x][i] = 0

# for i in range(19):
#     for j in range(19):
#         print(board[i][j], end = " ")
#     print()

# ### 6097
# h, w = input().split()
# w = int(w)
# h = int(h)
# board = [[0]*w for _ in range(h)]

# n = int(input())

# for _ in range(n):
#     l, d, x, y = input().split()
#     l = int(l)
#     d = int(d)
#     x = int(x) -1
#     y = int(y) -1

#     if d == 0:
#         for i in range(l):
#             if y + i < w:
#                 board[x][y + i] = 1
#     elif d==1:
#         for i in range(l):
#             if x + i < h:
#                 board[x + i][y] = 1

# for i in range(h):
#     for j in range(w):
#         print(board[i][j], end = " ")
#     print()

### 6098
board = [[0] * 10 for _ in range(10)]
for i in range(10):
    board[i] = list(map(int, input().split()))

x = 1
y = 1

while True:
    if board[y][x] == 2:
        board[y][x] = 9
        break
    elif board[y][x + 1] !=1:
        board[y][x] = 9
        x +=1
    elif board[y + 1][x] !=1:
        board[y][x] = 9
        y +=1
    else:
        board[y][x] = 9
        break

for i in range(10):
    for j in range(10):
        print(board[i][j], end = " ")
    print()

    ### commit test
    