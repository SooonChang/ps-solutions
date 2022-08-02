n = int(input())
array = list(map(int, input().split()))

def binary_fixed_point(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if mid == array[mid]:
        return mid
    
    elif mid > array[mid]:
        return binary_fixed_point(array, mid + 1, end)
    else:
        return binary_fixed_point(array, start, mid - 1)

result = binary_fixed_point(array, 0, n - 1)
if result == None:
    print(-1)
else:
    print(result)