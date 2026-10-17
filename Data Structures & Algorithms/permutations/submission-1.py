class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # if len(nums) == 0:
        #     return [[]]
        
        # perms = self.permute(nums[1:])
        # res = []
        # for p in perms:
        #     for i in range(len(p) + 1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)
        # return res

        permus = [[]]

        for n in nums:
            new_permus = []
            for p in permus:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_permus.append(p_copy)
            permus = new_permus
        return permus




