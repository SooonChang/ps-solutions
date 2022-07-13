### https://www.acmicpc.net/problem/10825

n = int(input())
data = []
for _ in range(n):
    stu_name, kor, eng, suri = input().split()
    kor = int(kor)
    eng = int(eng)
    suri = int(suri)
    data.append((stu_name, kor, eng, suri))

data.sort(key= lambda x: x[0])
data.sort(key = lambda x: x[3], reverse= True)
data.sort(key = lambda x: x[2])
data.sort(key = lambda x: x[1], reverse = True)

for i in data:
    print(i[0])