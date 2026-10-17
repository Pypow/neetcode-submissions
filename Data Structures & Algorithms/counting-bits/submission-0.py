class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for i in range(n + 1)]
        for i in range(n + 1):
            count = 0
            tmp = i
            while tmp:
                tmp = tmp & (tmp - 1)
                count += 1
            res[i] = count
        return res
             
            

