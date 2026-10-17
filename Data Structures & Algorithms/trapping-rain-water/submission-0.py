class Solution:
    def trap(self, height: List[int]) -> int:
        # T: O(N)   S: O(N)
        maxLeft = [0] * (len(height))
        maxRight = [0] * (len(height))
        res = 0

        for i in range(1, len(height)):
            j = len(height) -1 -i
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
            maxRight[j] = max(maxRight[j+1], height[j+1])

        for i, h in enumerate(height):
            bound = min(maxLeft[i], maxRight[i])
            if bound - h > 0:
                res += bound - h

        return res
