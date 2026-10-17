class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return int(tokens[0])
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(c))
        return stack[0]
