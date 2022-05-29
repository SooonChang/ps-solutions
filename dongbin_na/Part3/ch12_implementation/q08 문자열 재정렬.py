### try 01
# array = list(input())
# buffer = []
# sum_v = 0
# for i in array:
#     if ord('0') <= ord(i) < ord('9'):
#         sum_v += int(i)
#     else:
#         buffer.append(i)
# buffer.sort()
# for i in buffer:
#     print(i,end="")
# if sum_v !=0:
#     print(sum_v)
# else:
#     print()

### solution
from multiprocessing.sharedctypes import Value


array = input()
result = []
sum_v = 0

for x in array:
    if x.isalpha():
        result.append(x)
    else:
        sum_v +=int(x)

result.sort()

if sum_v != 0:
    result.append(str(sum_v))

print(''.join(result))