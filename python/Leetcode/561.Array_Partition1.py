# Runtime: 327 ms, faster than 17.56% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.9 MB, less than 31.92% of Python3 online submissions for Array Partition I.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(0,len(nums), 2):
            ans += nums[i]
        return ans
        

# # Runtime: 323 ms, faster than 18.02% of Python3 online submissions for Array Partition I.
# # Memory Usage: 16.7 MB, less than 68.22% of Python3 online submissions for Array Partition I.
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         return sum(sorted(nums)[::2])


# # Runtime: 410 ms, faster than 9.07% of Python3 online submissions for Array Partition I.
# # Memory Usage: 16.9 MB, less than 31.92% of Python3 online submissions for Array Partition I.
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         sum = 0
#         nums.sort()
        
#         for i, n in enumerate(nums):
#             if i % 2 == 0:
#                 sum += n
#         return sum


# # Runtime: 406 ms, faster than 9.53% of Python3 online submissions for Array Partition I.
# # Memory Usage: 16.8 MB, less than 68.22% of Python3 online submissions for Array Partition I.
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         sum = 0
#         pair = []
#         nums.sort()
        
#         for n in nums:
#             pair.append(n)
#             if len(pair) == 2:
#                 sum += min(pair)
#                 pair = []
#         return sum