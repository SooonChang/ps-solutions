### try 1
# n, m = map(int, input().split())

# ball_list = list(map(int, input().split()))

# result = 0

# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if ball_list[i] != ball_list[j]:
#             result += 1

# print(result)

### try 2
n, m = map(int, input().split())
ball = list(map(int, input().split()))
ball_list = [0] * (m + 1)

for i in ball:
    ball_list[i] += 1

result = 0

for i in range(1, m + 1):
    n -= ball_list[i]
    result += ball_list[i] * n

print(result)