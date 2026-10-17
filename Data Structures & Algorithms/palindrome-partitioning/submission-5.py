class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []

        def isPali(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(sub.copy())
                return
            
            for j in range(i, len(s)):  # IMP: use for loop to expand on palindromes
                if isPali(i, j):
                    sub.append(s[i: j+1])
                    dfs(j + 1)
                    sub.pop()           # no need to call dfs again
        dfs(0)
        return res
                




        