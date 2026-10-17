class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix)-1, len(matrix[0])-1
        
        top, bottom = 0, rows 
        row = 0
        l, r = 0, len(matrix[0])-1
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][l] > target:
                bottom = row - 1
            elif matrix[row][r] < target:
                top = row + 1
            else:
                break
        
        while l <= r:
            m = (l+r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False
            
            