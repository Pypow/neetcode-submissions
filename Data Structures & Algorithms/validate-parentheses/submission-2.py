class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if stack:
                if stack[-1] == "[" and b == "]":
                    stack.pop()
                elif stack[-1] == "(" and b == ")":
                    stack.pop()
                elif stack[-1] == "{" and b == "}":
                    stack.pop()
                else:
                    stack.append(b)
            else:
                stack.append(b)
        if stack:
            return False
        return True
            
            