class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k   # get index
        def quickSelect(l, r):
            p, piviot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= piviot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]

            if k < p: # res in left portion
                return quickSelect(l, p-1)
            elif k > p:  # res in right portion
                return quickSelect(p+1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums)-1)
