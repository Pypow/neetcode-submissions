class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(stack, openN, closeN):
            if closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(stack, openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(stack, openN, closeN + 1)
                stack.pop()
        backtrack([], 0, 0)
        return res            