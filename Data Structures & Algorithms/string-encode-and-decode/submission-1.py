class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i,s in enumerate(strs):
            tmp = []
            for c in s:
                res.append(c)
            res.append("_0_")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        tmp = []
        while i < len(s):
            c = s[i]
            if c == "_" and i + 2 < len(s) and s[i:i + 3] == "_0_":
                i += 3
                res.append("".join(tmp))
                tmp = []
                continue
            tmp.append(c)
            i += 1
        return res