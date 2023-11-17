def solution(k, score):
    tmp = []
    ans = []
    for s in score:
        if len(tmp) < k:
            tmp.append(s)
        elif min(tmp) < s:
            tmp.append(s)
            tmp.remove(min(tmp))
        ans.append(min(tmp))
    return ans