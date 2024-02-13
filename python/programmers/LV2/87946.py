from itertools import permutations
def solution(k, dungeons):
    pool = permutations(dungeons, len(dungeons))
    ans = []
    for case in pool:
        tmp_k = k
        tmp_ans = 0
        for std, con in case:
            if tmp_k >= std:
                tmp_k -= con
                tmp_ans += 1
        ans.append(tmp_ans)
            
    return max(ans)
    