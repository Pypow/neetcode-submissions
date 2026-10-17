class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hmap = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        sub = []

        def dfs(i):
            if len(sub) == len(digits):
                res.append("".join(sub))
                return
            if i >= len(digits):
                return
            for c in hmap[digits[i]]:
                sub.append(c)
                dfs(i + 1)
                sub.pop()
                dfs(i + 1)
        dfs(0)
        return res
