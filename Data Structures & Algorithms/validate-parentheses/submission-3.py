class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeMap = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in closeMap:
                if stack and stack[-1]==closeMap[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)
        return not stack
            