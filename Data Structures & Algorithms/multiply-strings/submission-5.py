class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # solve this problem like manual 2 digit multiplication
        # at each calculation, put carry and last digit at appropriate places
        # remove leading zeroes (unused placeholder in res)
        # reverse the res and return (we solve from right but, idx starts from left)
       
        # IMP: i1 + i2 is where result should be written to
       
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                product = int(num1[i1]) * int(num2[i2])  # IMP: if this is not allowd, use hmap
                res[i1 + i2] += product                  # tmp add full product
                res[i1 + i2 + 1] += res[i1 + i2] // 10   # IMP: use += res[i1 + i2] not += product| carry to next idx
                res[i1 + i2] = res[i1 + i2] % 10         # only last digit
        
        # remove leading zeroes after reversing res
        i = 0
        res = res[::-1]
        while i < (len(num1) + len(num2)) and res[i] == 0:
            i += 1
        # convert str arr to int arr
        res = map(str, res[i:])

        return "".join(res)


                
