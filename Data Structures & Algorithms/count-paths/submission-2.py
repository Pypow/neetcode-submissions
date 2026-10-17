class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r, c = m, n
        row = [1] * c
        for p in range(r - 1):
            newRow = [1] * c
            for i in range(c - 2, -1, -1):
                newRow[i] = newRow[i + 1] + row[i]
            row = newRow
        return row[0]

        