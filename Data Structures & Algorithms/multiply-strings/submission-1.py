class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))
        hmap = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = hmap[num1[i]] * hmap[num2[j]]
                res[i + j] += digit
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10
        
        res, beg = res[::-1], 0

        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)


