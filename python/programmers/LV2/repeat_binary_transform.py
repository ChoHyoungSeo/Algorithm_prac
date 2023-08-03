from collections import Counter
def solution(s):
    answer = []
    cnt = 0
    zeros = 0
    while True:
        ones = Counter(s)['1']
        zeros += Counter(s)['0']
        if ones == 1:
            cnt += 1
            break
        s = format(ones, 'b')
        cnt += 1
    answer.append(cnt)
    answer.append(zeros)
    return answer