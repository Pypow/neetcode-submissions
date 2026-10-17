class Solution:
    def isValid(self, s: str) -> bool:
        mapH = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        if s[0] in mapH:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] not in mapH:
                stack.append(s[i])
            else:
                if stack and mapH[s[i]] != stack[-1]:
                    return False
                if stack:
                    stack.pop()
        return True if not stack else False