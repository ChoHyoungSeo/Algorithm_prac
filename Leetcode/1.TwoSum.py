#should improve
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            tmp_tar = target - nums[i]
            tmp_num = nums[i]
            nums.remove(nums[i])
            if tmp_tar in nums:
                ans.append(i)
                ans.append(nums.index(tmp_tar)+1)
                break
            else:
                nums.insert(i,tmp_num)
        return ans