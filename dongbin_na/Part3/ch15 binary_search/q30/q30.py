###  첫 번째 풀이 (오답)
# def refine_word(word):
#     idx = 0
#     if word[0] == '?':
#         while word[idx] == '?':
#             idx += 1
#         keyword = word[idx:]
#         return keyword[::-1]
    
#     elif word[-1] == '?':
#         idx = -1
#         while word[idx] == '?':
#             idx -= 1
#         keyword = word[:(idx + 1)]
#         return keyword
#     else:
#         return []

# def find_first(words, w, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
    
#     n = len(w)
#     tmp = words[mid][:n]
#     if (mid == 0 or words[mid - 1][:n] < w) and words[mid][:n] == w:
#         return mid
#     elif words[mid][:n] >= w:
#         return find_first(words, w, start, mid - 1)
#     else:
#         return find_first(words, w, mid + 1, end)

# def find_last(words, w, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     n = len(w)
    
#     if (mid == len(words) -1 or words[mid + 1][:n] > w) and words[mid][:n]== w:
#         return mid
#     elif words[mid][:n] > w:
#         return find_last(words, w, start, mid -1)
#     else:
#         return find_last(words, w, mid + 1, end)

# def count_value(words, w):
#     first_idx = find_first(words, w, 0, len(words) - 1)
    
#     if first_idx == None:
#         return 0

#     last_idx = find_last(words, w, 0, len(words) - 1)
    
#     return last_idx - first_idx + 1

# def solution(words, queries):
#     rev_words = []
#     for i in words:
#         tmp = i[::-1]
#         rev_words.append(tmp)
#     words.sort()
#     rev_words.sort()
#     answer = []
#     for w in queries:
#         keyword = refine_word(w)
#         if w[-1] == '?':
#             answer.append(count_value(words, keyword))
#         else:
#             answer.append(count_value(rev_words, keyword))
#     return answer

# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

# print(solution(words, queries))

### 동빈나 풀이
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    
    for q in queries:
        if q[0] !='?':
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        answer.append(res)
        
    return answer