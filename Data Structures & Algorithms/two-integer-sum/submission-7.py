class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}   # diff: idx
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in hmap:
                return [hmap[nums[i]], i]
            hmap[diff] = i