# ### 3-1
# n = 1260
# count = 0
# coin_types = [500, 100, 50, 10]

# for coin in coin_types:
#     count += n //coin
#     n %= coin

# print(count)

### 3-2
# n, m, k = map(int, input().split())

# num_arr = list(map(int, input().split()))
# if len(num_arr) != n:
#     print("N개의 자연수")
#     exit()
# num_arr = sorted(num_arr, reverse=True)

# first = num_arr[0]
# second = num_arr[1]

# div = m // (k + 1)
# rem = m % (k + 1)

# res = first * (div * k + rem) + second * div
# print(res)

# ### 3-3
# n, m  = map(int, input().split())

# result = 0
# for _ in range(n):
#     data = list(map(int, input().split()))
#     minval = min(data)
#     result = max(result, minval)

# print(result)

# ### 3-4
# n, k = map(int, input().split())
# result = 0

# # while n >=k:
# #     while n % k != 0:
# #         n -= 1
# #         result +=1
    
# #     n //= k
# #     result += 1

# # while n > 1:
# #     n -= 1
# #     result +=1

# # print(result)
# ####################
# while True:
#     target = (n // k) * k
#     result += (n - target)
#     n = target

#     if n <k:
#         break
#     n //=k
#     result +=1
    
# result += n-1
# print(result)