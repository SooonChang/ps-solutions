### https://programmers.co.kr/learn/courses/30/lessons/60057
### try 01
# def cal_codec(s, inter):
#     i = 0
#     cnt = 1
#     n = len(s)
#     buffer = ""
#     prev_str = ""
#     now_str = ""
#     while i < n:
#         if i == 0:
#             prev_str = s[0:inter]
#             i += inter
#             continue
#         if i + inter <= n:
#             now_str = s[i:i+inter]
#         else:
#             now_str = s[i:n]
        
#         if prev_str == now_str:
#             cnt += 1
#         else:
#             if cnt > 1:
#                 buffer += str(cnt) + prev_str
#                 prev_str = now_str
#             else:
#                 buffer += prev_str
#                 prev_str = now_str
#             cnt = 1
#         i += inter
    
#     if cnt > 1:
#         buffer += str(cnt) + prev_str
#     else:
#         buffer += prev_str
    
#     return len(buffer)

# def solution(s):
#     n = len(s)
    
#     result = n
#     for i in range(1, n + 1):
#         tmp = cal_codec(s, i)
#         if tmp != 0 and tmp < result:
#             result = tmp
    
    
#     return result

### solution
from bz2 import compress


def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed +=str(count) + prev if count >=2 else prev
                prev = s[j:j+step]
                count = 1
        compressed +=str(count) + prev if count >=2 else prev
        answer = min(answer, len(compressed))
    
    return answer