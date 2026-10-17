class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix)    # bottom -> rows
        left, right = 0, len(matrix[0]) # right -> cols
        
        while left < right and top < bottom:
            # Top:  left to right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Right: top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                return res

            # Bottom: right to left
            for i in range(right - 1, left - 1, - 1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Left: bottom to top
            for i in range(bottom - 1, top - 1, - 1):
                res.append(matrix[i][left])
            left += 1
        return res