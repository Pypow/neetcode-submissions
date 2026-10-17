class Solution:
    def isHappy(self, n: int) -> bool:
        # helper
        def sumOfSq(n):
            res = 0
            while n:
                digit = n % 10
                digit = digit ** 2
                res += digit
                n = n // 10
            return res

        # fast and slow pointers
        slow = n
        fast = sumOfSq(n)
        while slow != fast:
            fast = sumOfSq(fast)
            fast = sumOfSq(fast)
            slow = sumOfSq(slow)
        return True if fast == 1 else False

