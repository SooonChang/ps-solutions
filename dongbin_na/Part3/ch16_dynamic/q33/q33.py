### 첫 번쨰 풀이
import sys
input = sys.stdin.readline
day = int(input())
data = []
dp = [0] * (day + 1)

for _ in range(day):
    data.append(list(map(int, input().split())))

for i in range(day - 1, -1, -1):
    t, p = data[i][0], data[i][1]

    if i + t <= day:
        dp[i] = max(dp[i + 1], dp[i + t] + p)
    else:
        dp[i] = dp[i + 1]

print(dp[0])