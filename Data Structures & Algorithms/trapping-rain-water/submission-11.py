class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        lmax, rmax = 0, 0
        l, r = 0, len(height)-1
        while l < r:
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                water = lmax - height[l]
                if water > 0:
                    res += water
                l += 1
            else:
                rmax = max(rmax, height[r])
                water = rmax - height[r]
                if water > 0:
                    res += water
                r -= 1
        return res

