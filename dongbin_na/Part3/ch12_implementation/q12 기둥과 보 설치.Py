### https://programmers.co.kr/learn/courses/30/lessons/60061
def solution(n, build_frame):
    answer = []
    for i in build_frame:
        data = [i[0], i[1], i[2]]
        if i[3] == 1 and build(n, data, answer):
            answer.append(data)
        elif i[3] == 0 and delete(data, answer):
            answer.remove(data)
    
    return answer

def build(n, data, result):
    result = False
    if data[2] == 0:
        result = build_bar(n, data, result)
    else:
        result = build_bo(n, data, result)
    
    return result

def delete(data, result):
    result = False
    if data[2] == 0:
        result = delete_bar(data, result)
    else:
        result = (delete_bo(data, result, -1) and delete_bo(data, result, 1))
    return result

def build_bar(n, data, result):
    x, y, a = data[0], data[1], data[2]
    if a != 0:
        return False
    
    if y == 0:
        return True
    if y + 1 > n:
        return False
    
    for i in result:
        px, py, pa = i[0], i[1], i[2]
        if pa == 0 and py == y - 1:
            return True
        elif pa == 1 and py == y and (px == x-1 or px == x):
            return True
    return False

def build_bo(n, data, result):
    x, y, a = data[0], data[1], data[2]
    if a != 1:
        return False
    if x + 1 > n:
        return False
    left = False
    right = False
    
    for c in result:
        px, py, pa = c[0], c[1], c[2]
        
        if pa == 0 and py == y-1 and (px == x or px == x + 1):
            return True
        elif pa == 1 and py == y and px == x - 1:
            left = True
        elif pa == 1 and py == y and px == x + 1:
            right = True
    
    if left and right:
        return True
    return False

def delete_bar(data, result):
    x, y, a = data[0], data[1], data[2]
    if a != 0:
        return False
    
    for i in result:
        px, py, pa = i[0], i[1], i[2]
        if pa == 0 and py == y + 1:
            return False
        elif pa == 1 and (px == x or px == x - 1):
            return delete_bo(i, result, 0)
    return True

def delete_bo(data, result, di):
    x, y, a = data[0], data[1], data[2]
    if a != 1:
        return False
    left = False
    right = False
    left_bar = False
    right_bar = False
    
    for i in result:
        px, py, pa = i[0], i[1], i[2]
        
        if pa == 1 and py == y and px == x -1: left = True
        elif pa == 1 and py == y and px == x + 1: right = True
        
        if pa == 0 and py == y -1 and px == x:
            left_bar = True
        elif pa == 0 and py == y -1 and px == x + 1:
            right_bar = True
    
    if left and right and di == 0:
        return True
    
    if left_bar and right == False:
        return True
    if right_bar and left == False:
        return True
    
    if di == 1 and right_bar:
        return True
    elif di == 1 and right:
        return delete_bo([x + 1, y, a], result, 1)
    if di == -1 and left_bar:
        return True
    elif di == -1 and left:
        return delete_bo([x -1, y, a], result, -1)
        
    return False

n = int(input())
build_frame = []
for i in range(8):
    build_frame.append(list(map(int, input().split())))

answer = solution(n, build_frame)
print(answer)