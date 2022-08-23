### 첫 번째 풀이
# import heapq
# n = int(input())

# buffer = []
# buffer.append(1)
# for i in range(n):
#     val = heapq.heappop(buffer)
#     if val * 2 not in buffer:
#         heapq.heappush(buffer, (val * 2))
#     if val * 3 not in buffer:
#         heapq.heappush(buffer, (val * 3))
#     if val * 4 not in buffer:
#         heapq.heappush(buffer, (val * 5))

# print(val)

### 두 번째 풀이
import heapq
n = int(input())

buffer = []
buffer.append(1)
cur_val = 1
next_val = 1
for i in range(n):
    cur_val = next_val
    heapq.heappush(buffer, (cur_val * 2))
    heapq.heappush(buffer, (cur_val * 3))
    heapq.heappush(buffer, (cur_val * 5))
    while cur_val == next_val:
        next_val = heapq.heappop(buffer)

print(cur_val)

### db_na
# n = int(input())
# ugly = [0] * n
# ugly[0] = 1 # 첫 번째 못생긴 수는 1
# i2 = i3 = i5 = 0 # 2배, 3배, 5배를 위한 인덱스

# next2, next3, next5 = 2, 3, 5 # 처음에 곱셈값을 초기화

# # 1부터 n까지의 못생긴 수를 찾기
# for i in range(1, n):
#     # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
#     ugly[i] = min(next2, next3, next5)

#     if ugly[i] == next2:
#         i2 += 1
#         next2 = ugly[i2] * 2
#     if ugly[i] == next3:
#         i3 += 1
#         next3 = ugly[i3] * 3
#     if ugly[i] == next5:
#         i5 += 1
#         next5 = ugly[i5] * 5

# print(ugly[n-1])
