class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif tokens[i] == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif tokens[i] == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif tokens[i] == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
            