class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # If nums[l] ≤ nums[m] (left sorted):
        #   target ∈ [nums[l],nums[m]) → r=m-1 else l=m+1
        # Else (right sorted):
        #   target ∈ (nums[m],nums[r]] → l=m+1 else r=m-1

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:      # IMP: (=) left sorted portion
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:                       # right sorted portion
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1