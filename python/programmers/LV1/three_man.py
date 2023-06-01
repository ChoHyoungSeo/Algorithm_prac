from itertools import combinations

def solution(number):
    answer = 0
    pool = combinations(number, 3)
    for num in list(pool):
        if sum(num) == 0:
            answer += 1
    return answer