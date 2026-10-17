class Solution:
    def myPow(self, x: float, n: int) -> float:
        negPow = True if n < 0 else False
        res = 1
        n = abs(n)

        if n == 0:
            return 1.00000

        while n:
            res *= x
            n -= 1
        return (1 / res) if negPow else res
