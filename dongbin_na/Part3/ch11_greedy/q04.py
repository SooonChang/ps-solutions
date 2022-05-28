### *** 그리디 익숙치 않은 문제 (보충 필요)
### mine
# n = int(input())
# array = list(map(int,input().split()))

# array.sort(reverse = True)
# dst = 1

# idx = 0
# while idx < n:
#     cost = dst
#     for i in range(idx, n):
        
#         if cost - array[i] == 0:
#             cost = 0
#             break
#         elif cost - array[i] < 0:
#             continue
#         else:
#             cost -= array[i]
#     if cost == 0:
#         idx = 0
#         dst += 1
#     else:
#         idx += 1

# print(dst)

### solution
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)