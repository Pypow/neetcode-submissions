class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # a // b is int division                (NOT THIS)
        # int(a / b) is truncates towards zero  (USE THIS)
        stack = []

        for t in tokens:
            if t == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif t == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))
        return stack[0]
