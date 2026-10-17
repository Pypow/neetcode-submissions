class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)
        res = 0
        for i in range(1, len(height)):
            j = len(height) - i - 1
            maxL[i] = max(height[i - 1], maxL[i - 1])
            maxR[j] = max(height[j + 1], maxR[j + 1])
        for i, h in enumerate(height):
            area = min(maxL[i], maxR[i]) - h
            if area > 0:
                res += area
        return res