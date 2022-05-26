### 7-1
### 순차 탐색
# def sequential_search(n, target, array):
#     for i in range(n):
#         if array[i] == target:
#             return i + 1

# print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")
# input_data = input().split()
# n = int(input_data[0])
# target = input_data[1]

# print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
# array = input().split()

# print(sequential_search(n, target, array))

### 7-2
### recursive binary search
# def binary_search_recursive(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
    
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search_recursive(array, target, start, mid -1)
#     else: return binary_search_recursive(array, target, mid + 1, end)

# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search_recursive(array, target, 0, n-1)
# if result == None:
#     print("None")
# else:
#     print(result + 1)

### 7-3
### iterative binary_search
# def binary_search_iter(array, target, start, end):

#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             start = mid + 1
#         else:
#             end = mid -1
    
#     return None

# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search_iter(array, target, 0, n-1)
# if result == None:
#     print("None")
# else:
#     print(result + 1)

### 7-4
### 빠르게 입력받기
import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)