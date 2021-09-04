#temp
import math
def solution(brown, yellow):
    brown = (brown // 2) -2
    temp = []

    for i in range(1,int(math.sqrt(yellow)+1)):
        if yellow % i == 0:
            tmp = []
            tmp.append(i)
            tmp.append(yellow//i)
        temp.append(tmp)

    for l in temp:
        if brown == sum(l):
            answer = list(map(lambda x : x+2, l))[::-1]

    return answer