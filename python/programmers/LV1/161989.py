from collections import deque
def solution(n, m, section):
    answer = 0
    section = deque(section)
    std = 0
    while section:
        tmp = section.popleft()
        if std <= tmp:
            std = tmp + m
            answer += 1
        
    return answer