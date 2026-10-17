class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        comb = []
        if not digits:
            return res
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

        def dfs(i):
            if len(comb) == len(digits):
                res.append("".join(comb))
                return
            if i >= len(digits):
                return 

            for c in hmap[digits[i]]:
                comb.append(c)
                dfs(i+1)
                comb.pop()
        dfs(0)
        return res
        
            
