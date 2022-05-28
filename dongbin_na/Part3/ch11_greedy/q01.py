n = int(input())
array = list(map(int, input().split()))
cnt = 0
result = 0
for i in array:
    cnt +=1
    if cnt >=i:
        cnt = 0
        result +=1
print(result)