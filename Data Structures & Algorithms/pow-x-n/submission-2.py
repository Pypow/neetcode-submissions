class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.00000
        
        inv = False
        if n < 0:
            inv = True
            n = n * -1
        
        res = x
        for i in range(n-1):
            res *= x
        return res if not inv else (1/res)
