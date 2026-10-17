class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for c in s:
            if c not in hmap:
                stack.append(c)
            else:
                if not stack or stack[-1] != hmap[c]:
                    return False
                else:
                    stack.pop()
        return False if stack else True