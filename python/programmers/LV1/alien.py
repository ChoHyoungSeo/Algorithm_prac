from itertools import permutations
def solution(spell, dic):
    answer = 0
    pool = permutations(spell)
    for word in pool:
        std = ''.join(list(word))
        if std in dic:
            return 1
    return 2