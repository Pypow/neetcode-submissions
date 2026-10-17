class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        res = 1
        for i in range(1, n):
            res = a + b
            a = b
            b = res
        return res
    

