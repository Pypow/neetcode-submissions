class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in ["(", "[", "{"]:
                stack.append(b)
            elif b == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif b == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            elif b == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
        return False if stack else True