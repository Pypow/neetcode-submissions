class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for b in s:
            if b in hmap:
                if not stack or stack[-1] != hmap[b]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(b)
        return True if not stack else False 