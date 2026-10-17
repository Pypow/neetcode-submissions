class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix)): # only swap half, other one will take care
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # reverse 
        for row in matrix:
            row.reverse()



