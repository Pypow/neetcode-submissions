class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 0 - 8 -> +1
        # 9 -> 0, +1 to prev (loop) if reached MSB, insert 1 at idx 0
        # T: O(n)                 n -> len of number
        # s: O(1)
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        carry = False
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carry = True
            else:
                carry = False
                digits[i] += 1
                return digits
        if carry:
            digits.insert(0, 1)
        return digits
            

        