### 첫 번째 풀이
# import sys
# import copy
# input = sys.stdin.readline

# n = int(input())
# data = []

# for i in range(n):
#     tmp = list(map(int, input().split()))
#     data.append(tmp)

# buffer = copy.deepcopy(data)
# for i in range(1, n):
#     for j in range(i + 1):
#         if j > 0:
#             buffer[i][j] = max(buffer[i][j], data[i][j] + buffer[i - 1][j - 1])
#         if j < i:
#             buffer[i][j] = max(buffer[i][j], data[i][j] + buffer[i - 1][j])

# print(max(buffer[n - 1]))

###  db_na
import sys
input = sys.stdin.readline
n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        
        dp[i][j] = dp[i][j] + max(up_left, up)
print(max(dp[n - 1]))