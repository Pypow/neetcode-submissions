class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        res = []

        def backtrack(subset, i):
            if len(subset) == len(digits):
                res.append("".join(subset))
                return
            
            for c in digitMap[digits[i]]:
                subset.append(c)
                backtrack(subset, i+1)
                subset.pop()

        if digits:
            backtrack([], 0)
        return res