class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if target > matrix[row][-1]:
                continue
            l, r = 0, len(matrix[0]) - 1
            while l <= r:
                m = (l + r) // 2
                if matrix[row][m] > target:
                    r = m - 1
                elif matrix[row][m] < target:
                    l = m + 1
                else:
                    return True
        return False