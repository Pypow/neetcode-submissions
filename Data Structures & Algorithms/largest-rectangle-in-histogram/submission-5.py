class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []  # h, startIdx

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, idx = stack.pop()
                area = height * (i - idx)
                res = max(res, area)
                start = idx
            stack.append((h, start))
        while stack:
            height, idx = stack.pop()
            res = max(res, (height) * (len(heights) - idx))
        return res