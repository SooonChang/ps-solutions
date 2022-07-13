def solution(N, stages):
    user_num = len(stages)
    data = [[0, 0] for _ in range(N + 1)]
    for i in range(N + 1):
        data[i][1] = i + 1
    
    for stage in stages:
        data[stage - 1][0] += 1
    
    for d in data:
        num = d[0]
        if user_num != 0:
            d[0] = d[0] / user_num
        else:
            d[0] = 0
        user_num -= num
    
    data.sort(key = lambda x:(-x[0], x[1]))
    answer = []
    for fail, idx in data:
        if 1<= idx <= N:
            answer.append(idx)
    
    return answer