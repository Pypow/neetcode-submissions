class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows-1

        while top <= bot:
            mrow = (top + bot) // 2
            if target > matrix[mrow][-1]:
                top = mrow + 1
            elif target < matrix[mrow][0]:
                bot = mrow - 1
            else:
                break
        
        if not (top <= bot):
            return False
        mrow = (top + bot) // 2
        l, r = 0, len(matrix[0])-1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mrow][mid]:
                l = mid + 1
            elif target < matrix[mrow][mid]:
                r = mid - 1
            else:
                return True
        return False
            