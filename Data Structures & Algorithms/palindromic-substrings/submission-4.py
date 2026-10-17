class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        # T: O(n^3)
        def getCount(i, count):
            nonlocal res
            if i >= len(s):
                return count
            for j in range(i, len(s)):
                if isPali(s[i:j+1]):
                    count += 1
            res += count
            getCount(i + 1, 0)
            return count

        def isPali(s):
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        getCount(0, 0)
        return res

