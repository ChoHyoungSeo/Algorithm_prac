# Runtime: 83 ms, faster than 43.70% of Python3 online submissions for Two Sum.
# Memory Usage: 15.4 MB, less than 20.82% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num]= i 


# Runtime: 104 ms, faster than 41.20% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 41.05% of Python3 online submissions for Two Sum.
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_map={}
#         for i, num in enumerate(nums):
#             nums_map[num] = i
#         for i, num in enumerate(nums):
#             if target - num in nums_map and i != nums_map[target - num]:
#                 return nums.index(num), nums_map[target-num]
            
            
# Runtime: 2214 ms, faster than 30.93% of Python3 online submissions for Two Sum.
# Memory Usage: 14.9 MB, less than 65.62% of Python3 online submissions for Two Sum.
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         ans = []
#         for i in range(len(nums)):
#             tmp_tar = target - nums[i]
#             tmp_num = nums[i]
#             nums.remove(nums[i])
#             if tmp_tar in nums:
#                 ans.append(i)
#                 ans.append(nums.index(tmp_tar)+1)
#                 break
#             else:
#                 nums.insert(i,tmp_num)
#         return ans