class Solution:
    def isValid(self, s: str) -> bool:
        mapClose = { ")": "(", "]": "[", "}": "{" }
        stack = []

        for c in s:
            if c in mapClose and len(stack)==0:
                return False
            if c in mapClose and mapClose[c] == stack[-1]:
                stack.pop()
                continue
            stack.append(c)
        return True if len(stack) == 0 else False
            


        