def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        tmp = t[i:i+len(p)]
        if int(tmp) <= int(p):
            answer += 1
    return answer