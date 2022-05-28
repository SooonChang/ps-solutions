### A-6
### 주요 라이브러리 문법과 유의점
# from itertools import permutations
# from math import perm
# from this import d
# data = ['A', 'B', 'C']

# result = list(permutations(data, 3))
# print(result)

# from itertools import combinations
# result = list(combinations(data, 2))
# print(result)

# from itertools import product
# result = list(product(data, repeat=2))
# print(result)

# import heapq
# from itertools import count

# def heapsort(iterable):
#     h = []
#     result = []

#     for value in iterable:
#         heapq.heappush(h, value)
    
#     for _ in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result

# result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
# print(result)

# from bisect import bisect_left, bisect_right
# a = [1, 2, 4, 4, 8]
# x = 4
# print(bisect_right(a, x))
# print(bisect_left(a, x))

# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     left_index = bisect_left(a, left_value)
#     return right_index - left_index

# a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
# print(count_by_range(a, 4, 4))
# print(count_by_range(a, -1, 3))

from collections import deque, Counter

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))
counter = Counter(data)
print(counter)