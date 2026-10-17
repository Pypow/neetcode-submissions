class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # LL cycle detection
        # Floyd's hare tortoise - begining of cycle:
        """ distance between fast & slow intersection and 
        start of the cycle == dist from 0th idx and start of the cycle
        """
        # LL cycle detection
        slow = nums[0]
        fast = nums[nums[0]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # Floyd's hare tortoise algo
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow2