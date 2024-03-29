def solution(n, lost, reserve):
    n_lost = list(set(lost) - set(reserve))
    n_reserve = list(set(reserve) - set(lost))
    answer = n - len(n_lost)
    
    for i in range(len(n_lost)):
        if (n_lost[i] - 1) in n_reserve:
            answer += 1
            n_reserve.remove(n_lost[i]-1)
        elif (n_lost[i] + 1) in n_reserve:
            answer += 1
            n_reserve.remove(n_lost[i]+1)
        else:
            continue
    return answer