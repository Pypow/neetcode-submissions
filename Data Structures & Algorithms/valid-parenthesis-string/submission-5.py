class Solution:
    def checkValidString(self, s: str) -> bool:
    # here we store valid range of solutions, this range is because of *s in input
    # leftMin -> what is the min open parentesis we can have depending on *
    # leftMin: worst case if we treat every * as ) what is the start of valid range
    # leftMax -> what is the max open parentesis we can have depending on *
    # leftMax: Best case if we treat every * as ( what is the end of valid range
        leftMin = 0
        leftMax = 0
        for c in s:
            if c == "(":    # left pare -> inc both
                leftMin += 1
                leftMax += 1
            elif c == ")":  # right pare -> matched open paren, decre both
                leftMin -= 1
                leftMax -= 1
            else:           # * -> can be "("" [incre max]  |  can be ")" [decre min]  
                leftMin -= 1
                leftMax += 1
            if leftMin < 0:
                leftMin = 0 # we were too harsh, so use some wildcards to make this 0
            if leftMax < 0:
                return False # can't recover, too many ")"
        return leftMin == 0 # if > 0, can't recover, too many "("