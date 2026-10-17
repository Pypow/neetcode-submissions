class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [-1 for i in range(len(height))]
        maxR = [-1 for j in range(len(height))]
        l = 0
        r = 0
        total = 0

        for i in range(len(height)):
            j = len(height) - i - 1
            l = max(l, height[i])
            r = max(r, height[j])
            maxL[i] = l
            maxR[j] = r

        for i, h in enumerate(height):
            water = min(maxL[i], maxR[i]) - h
            if water > 0:
                total += water
        return total     
