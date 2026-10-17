class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair = [(1, 4), (3, 2)]
        pair = [(p,s) for p, s in zip(position, speed)]
        stack = [] # time to reach destination

        for p, s in sorted(pair)[::-1]:
            if stack and stack[-1] >= ((target-p)/s):
                continue
            stack.append((target-p)/s)
        return len(stack)




