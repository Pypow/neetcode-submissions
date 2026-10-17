class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n+1):
            tmp = a
            a = a + b
            b = tmp
        return a