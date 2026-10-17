class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(reverse = True)

        for p, s in cars:
            time = (target - p) / s
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)
            