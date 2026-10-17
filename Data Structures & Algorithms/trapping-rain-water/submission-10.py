class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer solution
        l, r = 0, len(height) - 1
        total = 0
        maxL = 0
        maxR = 0
        while l < r:
            if height[l] <= height[r]:
                water = maxL - height[l]
                maxL = max(height[l], maxL)
                l += 1
                if water > 0:
                    total += water
            else:
                water = maxR - height[r] 
                maxR = max(height[r], maxR)
                r -= 1
                if water > 0:
                    total += water
        return total