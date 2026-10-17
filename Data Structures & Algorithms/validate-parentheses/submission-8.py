class Solution:
    def isValid(self, s: str) -> bool:
        mapH = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for c in s:
            if c not in mapH:
                stack.append(c)
            else:
                if not stack or stack[-1] != mapH[c]:
                    return False
                else:
                    stack.pop()
        return True if not stack else False
                
