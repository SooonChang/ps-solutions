# ### 6077
# n = int(input())
# s = 0
# for i in range(1, n+1):
#     if i%2==0:
#         s +=i
# print(s)

# ### 6078
# n = 0
# while n != 'q':
#     n = input()
#     print(n)

# ### 6079
# n = int(input())
# s = 0
# cnt = 0
# while s < n :
#     cnt+=1
#     s +=cnt
# print(cnt)

### 6080
# n, m = input().split()
# n = int(n)
# m = int(m)
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i,j)

# ### 6081
# # *** 16진수 입력으로 받기, 16진수 구구단
# n = int(input(), 16)
# for i in range(15):
#     print('%X'%n,'*%X'%(i+1),'=%X'%(n*(i+1)),sep="")

# ### 6082
# n = int(input())
# if n<1 or n>30:
#     exit()
# for i in range(1, n+1):
#     if i%10 == 3 or i%10 == 6 or i % 10 == 9:
#         print("X",end=' ')
#     else:
#         print(i, end=' ')

# ### 6083
# red, green, blue = input().split()
# red = int(red)
# green = int(green)
# blue = int(blue)
# cnt = 0

# if not(0<=red<=127 and 0<=green<=127 and 0<=blue<=127):
#     exit()
# for r in range(red):
#     for g in range(green):
#         for b in range(blue):
#             print(r,g,b)
#             cnt +=1
# print(cnt)

# ### 6084
# # ***특정 소수점까지 출력 하는 방법
# # round(fnum, 2)
# # format(fnum, ".2f")
# # "%.1f"%fnum
# # *** format을 주로 쓰자...
# h, b, c, s = input().split()
# h = int(h)
# b = int(b)
# c = int(c)
# s = int(s)

# if not(0< h <=48000 and 0<b<=32 and b%8==0 and 0<c<=5 and 0<s<=6000):
#     exit()

# mem = (h * b * c * s) / (8 * 1024 * 1024)
# print(round(mem, 1), "MB")
# print(format(mem, ".1f"),"MB")
# print("%.1f"%mem, "MB")

# ### 6085
# w, h, b = input().split()
# w = int(w)
# h = int(h)
# b = int(b)

# if not(0 < w <=1024 and 0< h <= 1024 and 0 < b <= 40 and b % 4 == 0):
#     exit()

# mem = (w * h * b) / (8 * 1024 * 1024)
# print(format(mem, ".2f"), "MB")

### 6086
# n = int(input())
# if n > 100000000:
#     exit()
# s = 0
# c = 1
# while True:
#     s += c
#     c += 1

#     if s>=n:
#         break
# print(s)

# ### 6087
# n = int(input())
# if n < 1 or n > 100:
#     exit()

# for i in range(1, n + 1):
#     if i % 3 == 0:
#         continue
#     else:
#         print(i, end = ' ')

# ### 6088
# a, d, n = input().split()
# a = int(a)
# d = int(d)
# n = int(n)
# res = a + (n-1)*d
# print(res)

# ### 6089
# a, r, n = input().split()
# a = int(a)
# r = int(r)
# n = int(n)
# if not(0<=a<=10 and 0<=r<=10 and 0<=n<=10):
#     exit()
# res = a*(r**(n-1))
# print(res)

# ### 6090
# a, m, d, n = input().split()
# a = int(a)
# m = int(m)
# d = int(d)
# n = int(n)
# if not(-50<=a<=50 and -50<=m<=50 and -50<=d<=50 and 0<n<=10):
#     exit()

# res = a
# for i in range(1, n):
#     res = res*m + d
# print(res)

### 6091
p1, p2, p3 = input().split()
p1 = int(p1)
p2 = int(p2)
p3 = int(p3)
d = 1
while d%p1!=0 or d%p2!=0 or d%p3!=0:
    d +=1
print(d)