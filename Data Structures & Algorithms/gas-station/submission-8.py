class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # logic: You only need to go till last idx, the cirular cond will be 
        # taken care by the sum(gas) > sum(cost) condition
        if sum(gas) < sum(cost):
            return -1

        def dfs(j, tank):
            if j == len(gas):
                return True
            tank += gas[j] - cost[j]
            if tank < 0:
                return False
            return dfs(j + 1, tank)

        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                if dfs(i, 0):
                    return i
        return -1