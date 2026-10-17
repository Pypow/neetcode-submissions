class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (r + l) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:  # left sorted portion
                l = m + 1
            else:                   # right sorted portion
                r = m - 1
        return res
            