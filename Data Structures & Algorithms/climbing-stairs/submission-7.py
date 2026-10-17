class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for i in range(1, n):
            tmp = a
            a = a + b
            b = tmp
        return a
