class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []
        def backtrack(opn, close):
            if opn == n and close == n:
                res.append("".join(sub))
                return
            if opn < n:                 # IMP: if it is eq, we must NOT add more
                sub.append("(")
                backtrack(opn + 1, close)
                sub.pop()                   
            
            if close < opn:             # IMP: if it is eq, we must NOT add more
                sub.append(")")         
                backtrack(opn, close + 1)
                sub.pop()               # in backtrack pop as soon as you recusive call
        backtrack(0, 0)
        return res

