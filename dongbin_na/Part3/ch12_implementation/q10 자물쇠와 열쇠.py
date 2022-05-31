### https://programmers.co.kr/learn/courses/30/lessons/60059
def rotate_matrix(a):
    n = len(a)
    m = len(a[0])
    
    new_matrix = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            new_matrix[j][n - i -1] = a[i][j]

    return new_matrix

def check(new_lock):
    length = len(new_lock) // 3
    
    for i in range(length):
        for j in range(length):
            if new_lock[length + i][length + j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    
    new_lock = [[0] * (3 * n) for _ in range(3 * n)]
    
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_matrix(key)
        
        for y in range(2 * n):
            for x in range(2 * n):
                
                for i in range(m):
                    for j in range(m):
                        new_lock[y + j][x + i] += key[j][i]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[y + j][x + i] -= key[j][i]
                        
    return False