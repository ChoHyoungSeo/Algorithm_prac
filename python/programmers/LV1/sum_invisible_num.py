def solution(numbers):
    nums = [x for x in range(10)]
    ans = set(nums) - set(numbers)
    if not ans:
        return 0
    else:
        return sum(ans)