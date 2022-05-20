# ### 6065
# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)

# if a%2 == 0:
#     print(a)
# if b%2 == 0:
#     print(b)
# if c%2 == 0:
#     print(c)

# ### 6066
# a, b, c = input().split()
# n = [int(a), int(b), int(c)]

# for i in n:
#     if i%2 == 0:
#         print("even")
#     else:
#         print("odd")

# ### 6067
# n = int(input())

# if n < 0:
#     if n%2 == 0:
#         print('A')
#     else:
#         print('B')
# else:
#     if n%2 ==0:
#         print('C')
#     else:
#         print('D')

# ### 6068
# n = int(input())
# if n>=90 :
#   print('A')
# else :
#   if n>=70 :
#     print('B')
#   else :
#     if n>=40 :
#       print('C')
#     else :
#       print('D')

# ### 6069
# c = input()
# if c == 'A':
#     print("best!!!")
# elif c == 'B':
#     print("good!!")
# elif c == 'C':
#     print("run!")
# elif c == 'D':
#     print("slowly~")
# else:
#     print("what?")

### 6070
n = int(input())
if n <=0 or n>12:
    exit()
elif n == 12 or n ==1 or n == 2:
    print("winter")
elif n == 3 or n ==4 or n == 5:
    print("spring")
elif n == 6 or n == 7 or n == 8:
    print("summer")
elif n == 9 or n == 10 or n == 11:
    print("fall")