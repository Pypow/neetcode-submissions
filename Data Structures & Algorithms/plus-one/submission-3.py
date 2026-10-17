class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # LSB < 9 -> +1
        # while LSB == 9 -> digits[i] = 0, digits[i-1] += 1

        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    return digits
                else:
                    i -= 1
            else:
                digits[i] += 1
                return digits
