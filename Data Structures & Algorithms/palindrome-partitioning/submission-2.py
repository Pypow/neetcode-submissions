class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []
        def dfs(i):
            if i >= len(s):
                res.append(sub.copy())
                return  

            for idx in range(i, len(s)):
                if (isPali(s[i:idx+1])):
                    sub.append(s[i:idx+1])
                    dfs(idx+1)
                    sub.pop()

        def isPali(word):
            if not word:
                return False
            l, r = 0, len(word)-1
            while l <= r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        dfs(0)
        return res
