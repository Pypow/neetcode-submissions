class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]  # temp, idx
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                t, idx = stack[-1]
                res[idx] = i - idx
                stack.pop()
            stack.append((temperatures[i], i))
        return res

            