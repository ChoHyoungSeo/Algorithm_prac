from collections import Counter
def solution(n):
    answer = 0
    i = 1
    target = n
    bin_n = bin(n)
    std = Counter(bin_n)['1']
    while True:
        target += i
        bin_target = bin(target)
        ones = Counter(bin_target)['1']
        if std == ones:
            answer = target
            break
    return answer