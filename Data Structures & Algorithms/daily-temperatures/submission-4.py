class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [(temperatures[0], 0)] # (tmp, idx)
        for i in range(1, len(temperatures)):
            t = temperatures[i]
            while stack and stack[-1][0] < t:
                tem, idx = stack.pop()
                res[idx] = i - idx
            stack.append((t, i))
        return res




            
