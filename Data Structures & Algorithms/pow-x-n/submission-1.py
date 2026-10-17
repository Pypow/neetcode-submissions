class Solution:
    def myPow(self, x: float, n: int) -> float:
        negPow = False
        if n == 0:
            return 1.0000
        if x == 0:
            return 0
        if n < 0:
            negPow = True
        n = abs(n)
        res = 1
        for i in range(n):
            res *= x

        if negPow:
            res = 1 / res
        return res