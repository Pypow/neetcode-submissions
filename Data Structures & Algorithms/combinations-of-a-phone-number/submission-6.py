class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        sub = []

        def dfs(i):
            if len(sub) == len(digits):
                res.append("".join(sub))
                return
            for c in hmap[digits[i]]:
                sub.append(c)
                dfs(i + 1)
                sub.pop()
        dfs(0)
        return res






        
            