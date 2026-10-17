class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 0
        for i in range(n):
            tmp = a
            a = a + b
            b = tmp
        return a
