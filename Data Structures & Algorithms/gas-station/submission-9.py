class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # logic: You only need to go till last idx, the cirular cond will be 
        # taken care by the sum(gas) > sum(cost) condition

        # GREEDY: if ith idx fails, the whole path is failed
        if sum(gas) < sum(cost):
            return -1
        res = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1     # IMP: we don't need to check intermidiate i's, from starting point

        return res