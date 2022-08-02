### 첫번째 풀이
# n, x = map(int, input().split())
# data = list(map(int, input().split()))

# def binary_search(array, target, start, end, dir):
#     if start > end:
#         return None
#     mid = (start + end) // 2

#     if array[mid] == target:
#         if 0 <= (mid + dir) < n and array[mid + dir] != target:
#             return mid
#         elif (mid + dir) < 0 or (mid + dir) >= n:
#             return mid
#         elif dir == -1:
#             return binary_search(array, target, start, mid - 1, dir)
#         elif dir == 1:
#             return binary_search(array, target, mid + 1, end, dir)

#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1, dir)
#     elif array[mid] < target:
#         return binary_search(array, target, mid + 1, end, dir)

# left = binary_search(data, x, 0, n - 1, -1)
# right = binary_search(data, x, 0, n - 1, 1)

# if left == None and right == None:
#     print(-1)
# else:
#     print(right - left + 1)

### 동빈나 풀이
# # 처음 위치를 찾는 이진 탐색 메서드
# def first(array, target, start, end):
#     if start > end:
#         return None
    
#     mid = (start + end) // 2
#     # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
#     if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
#         return mid
#     # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
#     elif array[mid] >= target:
#         return first(array, target, start, mid - 1)
#     # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인    
#     else:
#         return first(array, target, mid + 1, end)

# # 마지막 위치를 찾는 이진 탐색 메서드
# def last(array, target, start, end):
#     if start > end:
#         return None
    
#     mid = (start + end) // 2
#     # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
#     if (mid == (len(array) - 1) or target < array[mid + 1]) and array[mid] == target:
#         return mid
#     # 중간점의 값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#     elif array[mid] > target:
#         return last(array, target, start, mid - 1)
#     # 중간점의 값 보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
#     else:
#         return last(array, target, mid + 1, end)


# def count_by_value(array, x):
#     # 데이터의 개수
#     n = len(array)

#     # x가 처음 등장한 인덱스 계산
#     a = first(array, x, 0, n - 1)

#     if a == None:
#         return -1
    
#     # x가 마지막으로 등장한 인덱스 계산
#     b = last(array, x, 0, n - 1)

#     return b  - a + 1

# n, x = map(int, input().split())
# array = list(map(int, input().split()))

# count = count_by_value(array, x)
# print(count)

### 동빈나 라이브러리 사용
### bisect 라이브러리
from bisect import bisect_left, bisect_right
# 값이 [left_value, right_value]인 데이터 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)
if count == 0:
    print(-1)
else:
    print(count)
