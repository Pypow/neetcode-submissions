class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)
        for n in nums:
            if (n-1) not in numset:     # IMP - optimizes solution
                length = 0
                while (n + length) in numset:
                    length += 1 
                res = max(res, length)
        return res




