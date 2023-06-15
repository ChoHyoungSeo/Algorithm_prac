def solution(slice, n):
    ans = n // slice
    if n % slice:
        ans += 1
    return ans