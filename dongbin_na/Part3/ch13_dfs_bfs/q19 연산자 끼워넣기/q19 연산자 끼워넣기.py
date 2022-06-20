### https://www.acmicpc.net/problem/14888
# INF = int(1e9)
# n = int(input())
# equation = list(map(int, input().split()))
# oper = list(map(int, input().split()))

# min_val = INF
# max_val = -INF

# def operation(a, b, oper):
#     if oper == 0:
#         return a + b
#     elif oper == 1:
#         return a - b
#     elif oper == 2:
#         return a * b
#     elif oper == 3:
#         return int(a / b)
#     else:
#         exit(-1)

# def dfs(cnt, res):
#     global min_val
#     global max_val

#     if cnt == n:
#         min_val = min(min_val, res)
#         max_val = max(max_val, res)
#     else:
#         for i in range(len(oper)):
#             if oper[i] > 0:
#                 oper[i] -= 1
#                 tmp = operation(res, equation[cnt], i)
#                 dfs(cnt + 1, tmp)
#                 oper[i] += 1

# dfs(1, equation[0])

# print(max_val)
# print(min_val)

### 동빈나
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val = 1e9
max_val = -1e9

def dfs(i, now):
    global min_val, max_val, add, sub, mul, div

    if i == n:
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1
dfs(1, data[0])
print(max_val)
print(min_val)