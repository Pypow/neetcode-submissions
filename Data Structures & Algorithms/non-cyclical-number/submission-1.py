class Solution:
    def isHappy(self, n: int) -> bool:

        def getDigitSum(num):
            total = 0
            while num:
                digit = num % 10
                num = int(num / 10)
                total += digit ** 2
            return total

        slow = n
        fast = getDigitSum(n)

        while fast != 1 and fast != slow:
            slow = getDigitSum(slow)
            fast = getDigitSum(getDigitSum(fast))
        
        return fast == 1


            
        
