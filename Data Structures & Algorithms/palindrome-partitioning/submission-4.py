class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []
        if not s:
            return []
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
            for j in range(i, len(s)):
                if isPali(i, j):
                    sub.append(s[i:j+1])
                    dfs(j + 1)
                    sub.pop()
        dfs(0)
        return res

        

            