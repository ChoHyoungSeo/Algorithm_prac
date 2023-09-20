# timeout
# from itertools import permutations
# def solution(n, k):
#     nums = [x for x in range(1, n+1)]
#     pool = list(permutations(nums, n))
#     # pool.sort()
#     return pool[k-1]
import math
def solution(n, k):
    
    nums = [i for i in range(1, n + 1)]
    k -= 1  # 0-based index
    res = []
    
    for i in range(n, 0, -1):
        idx = k // math.factorial(i - 1)
        k %= math.factorial(i - 1)
        
        res.append(nums[idx])
        del nums[idx]
        
    return res
