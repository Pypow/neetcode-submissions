class Solution:
    def climbStairs(self, n: int) -> int:
        # dp solution
        n1, n2 = 1, 0
        for i in range(n):
            tmp = n1
            n1 = n1 + n2
            n2 = tmp
        return n1