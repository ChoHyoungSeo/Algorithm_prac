def solution(num):
    answer = 0
    if num == 1:
        return 0
    for _ in range(1, 501):
        if num % 2 == 0:
            num //= 2
            answer += 1
        else:
            num = num * 3 + 1
            answer += 1
        
        if num == 1:
            return answer
    
    return -1