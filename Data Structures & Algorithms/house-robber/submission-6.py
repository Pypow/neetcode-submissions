class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0
        # [r1, r2, n, n-1, n-2, ...]
        for n in nums:
            tmp = max(r1 + n, r2)
            r1 = r2
            r2 = tmp
        return r2
            