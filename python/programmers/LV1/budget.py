def solution(d, budget):
    answer = 0
    d.sort()
    for num in d:
        budget -= num
        answer += 1
        if budget < 0:
            answer -= 1
            break
    return answer