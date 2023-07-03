def solution(absolutes, signs):
    ans = 0
    for num, sign in zip(absolutes, signs):
        if not sign:
            num = -num
        ans += num
    return ans