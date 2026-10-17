class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        res = 0
        for n in nums:
            count = 1
            if (n-1) in nums:
                continue
            ele = n
            while (ele + 1) in nums:
                ele = ele + 1
                count += 1
            res = max(res, count)
        return res
"""
    T: O(n)
    S: O(n)"""