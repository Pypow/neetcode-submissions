class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = set()
        for n in nums:
            if n in hmap:
                return True
            hmap.add(n)
        return False