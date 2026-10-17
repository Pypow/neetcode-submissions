class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def getDigitSum(num):
            total = 0
            while num:
                digit = num % 10
                num = int(num / 10)
                total += digit ** 2
            return total


        while n > 1:
            n = getDigitSum(n)
            if n in visit:
                return False
            visit.add(n)
        return True if n == 1 else False


            
        
