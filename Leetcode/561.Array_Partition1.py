# Runtime: 327 ms, faster than 17.56% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.9 MB, less than 31.92% of Python3 online submissions for Array Partition I.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(0,len(nums), 2):
            ans += nums[i]
        return ans