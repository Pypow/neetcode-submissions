class Solution:
    def checkValidString(self, s: str) -> bool:
        # stack solution
        # T: O(n) | S: O(n)
        opening = []
        star = []

        for i, c in enumerate(s):
            if c == "(":
                opening.append(i)
            elif c == "*":
                star.append(i)
            else:
                if not opening and not star:
                    return False
                if opening:
                    opening.pop()
                else:
                    star.pop()
        
        while opening and star:
            if opening.pop() > star.pop():
                return False
        return not opening
        