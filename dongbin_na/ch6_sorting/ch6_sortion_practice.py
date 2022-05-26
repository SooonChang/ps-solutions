### 6-10
# n = int(input())
# array = []
# for _ in range(n):
#     array.append(int(input()))

# array.sort(reverse=True)
# for i in range(len(array)):
#     print(array[i], end=' ')

### 6-11
# n = int(input())
# array = []
# for _ in range(n):
#     array.append(list(input().split()))

# # def key(data):
# #     return int(data[1])

# # array = sorted(array, key= key)
# array = sorted(array, key=lambda student: student[1])
# for i in range(len(array)):
#     print(array[i][0], end=" ")

### 6-12
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))