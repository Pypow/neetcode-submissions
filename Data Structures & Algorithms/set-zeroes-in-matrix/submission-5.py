class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # T -> O(R*C)  |  S -> O:(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # record zeros 
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        # mark zeros in rest of the matrix, except 1st row and col
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # mark first row and cols as zero

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        if rowZero:                 # IMP: order matters, this should come second
            for c in range(COLS):
                matrix[0][c] = 0
            
