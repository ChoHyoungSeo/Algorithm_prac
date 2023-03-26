def solution(n):
    ans = []
    for i in range(n):
        tmp = i*2+1
        if tmp > n:
            break
        ans.append(tmp)
    return ans