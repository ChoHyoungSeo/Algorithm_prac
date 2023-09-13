from itertools import combinations
def solution(numbers):
    answer = set()
    tmp = list(combinations(numbers, 2))
    for x, y in tmp:
        answer.add(x+y)
        
    return sorted(list(answer))