class Solution:
    def countSum(self, digit):
        total = 0
        while digit:
            d = digit % 10
            digit = digit// 10
            total += d ** 2
        return total
    
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.countSum(n)

        while fast != 1 and slow != fast:
            slow = self.countSum(slow)
            fast = self.countSum(self.countSum(fast))
        return fast == 1

