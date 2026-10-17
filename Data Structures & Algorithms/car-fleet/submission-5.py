class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [[p, s] for p, s in zip(position, speed)]
        fleet.sort()
        stack = []

        for i in range(len(fleet)-1, -1, -1):
            p, s = fleet[i][0], fleet[i][1]
            dist = target - p
            time = dist / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack)