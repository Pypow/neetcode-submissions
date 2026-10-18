class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}      # diff: idx
        for i in range(len(nums)):
            if nums[i] in hmap:
                return [hmap[nums[i]], i]
            diff = target - nums[i]
            hmap[diff] = i
        return [-1, -1]