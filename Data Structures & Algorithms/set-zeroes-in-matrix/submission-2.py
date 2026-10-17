class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = False
        rows, cols = len(matrix), len(matrix[0])

        #   mark header rows & cols
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        # change to zeros in main matrix according to headers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # change header row & col to zero
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
        
        
        
        