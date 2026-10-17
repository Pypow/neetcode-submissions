class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # only opening closing brackets
        hmap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c not in hmap:
                stack.append(c)
                continue
            if not stack or hmap[c] != stack[-1]:
                return False
            stack.pop()
        return True if not stack else False