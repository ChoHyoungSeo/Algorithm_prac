def solution(nums):
    max_ans = int(len(nums) / 2)
    filtered = set(nums)
    if len(filtered) > max_ans:
        return max_ans
    else:
        return len(filtered)