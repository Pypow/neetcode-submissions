class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We can do using max heap + pop k times -> T: O(n + K log(n))
        # Quick Select: (partial sorting) -> T: O(n) avg, T: O(n^2) worst
        # pick a piviot (e.g right most) and pointer p at 0, compare ele from [: n-1]:
        #       if less than piviot -> swap with pointer p
        #       else -> leave it as it is. At the end, swap pivot and p
        # if p == k then reuturn res else redo the loop at n-2 as pivot (right most)
        k = len(nums) - k   # get idx
        
        def quickSelect(l, r):
            piviot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= piviot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]     # swap p with piviot
            if k > p:
                return quickSelect(p + 1, r)
            elif k < p:
                return quickSelect(l, p - 1)
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1)