def solution(k, m, score):
    answer = 0
    start = 0
    score.sort(reverse=True)
    for _ in range(len(score) // m):
        answer += min(score[start:start + m]) * m
        start += m
    
    return answer