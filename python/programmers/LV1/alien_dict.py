from itertools import permutations
def solution(spell, dic):
    answer = 0
    pool = permutations(spell)
    for word in pool:
        std = ''.join(list(word))
        if std in dic:
            return 1
    return 2
##
def solution(spell, dic):
    for word in dic:
        tmp = 0
        for s in spell:
            if s in word:
                tmp += 1
        if tmp == len(word) and tmp == len(spell):
            return 1
    return 2