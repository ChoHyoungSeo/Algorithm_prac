def solution(s):
    ans = 0
    for tmp in s:
        if ans < 0:
            return False
        if tmp == "(":
            ans += 1
        else:
            ans -= 1
    if ans != 0:
        return False
    return True