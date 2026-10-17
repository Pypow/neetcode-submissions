class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []      # [idx, h]
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = (i - index) * height
                res = max(res, area)
                start = index
            stack.append([start, h])
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res

                