def solution(n, words):
    answer = []
    cnt = 1
    turn = 1
    pool = []
    flag = False
    
    for i in range(len(words)):
        if i == 0:
            pool.append(words[i])
            continue
        elif cnt > n:
            turn += 1
            cnt = 1
        if words[i][0] == words[i-1][-1] and words[i] not in pool:
            cnt += 1
            pool.append(words[i])
        else:
            flag = True
            cnt += 1
            break
        
    if flag:
        if cnt > n:
            turn += 1
            cnt = 1
        return [cnt, turn]
    else:
        return [0,0]