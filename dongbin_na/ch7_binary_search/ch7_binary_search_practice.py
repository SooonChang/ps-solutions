### 7-2
# n = int(input())
# n_array = list(map(int, input().split()))

# m = int(input())
# m_array = list(map(int, input().split()))

# def binary_search(array, target):
#     start = 0
#     end = len(array) - 1

#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return True
#         elif array[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return False

# n_array.sort()

# for i in m_array:
#     if binary_search(n_array, i):
#         print("yes", end = " ")
#     else:
#         print("no", end = " ")

### 7-3
n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

h_start = 0
h_end = array[-1]
result = -1

while h_start <= h_end:
    h = (h_start + h_end) // 2
    sum = 0

    for i in array:
        sum += max(0, i - h)
    
    if sum < m:
        h_end = h - 1
    elif sum >= m:
        h_start = h + 1
        if result < h:
            result = h
        
print(result)
