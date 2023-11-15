# from collections import Counter
from collections import defaultdict

def solution(k, tangerine):
    cnt = 0
    ddict = defaultdict(int)
    for num in tangerine:
        ddict[num] += 1
    for _, v in sorted(ddict.items(), key=lambda x: x[-1], reverse=True):
        k -= v
        cnt += 1
        if k <= 0:
            break
    return cnt