class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []      # "neet_|_code_|_love_|_you_|_"
        for word in strs:
            for c in word:
                s.append(c)
            s.append("_|_")
        return "".join(s)

    def decode(self, s: str) -> List[str]:
        res = []
        word = []
        i = 0
        while i < len(s):
            if (i + 3) <= len(s) and s[i] == "_" and s[i: i+3] == "_|_":    # IMP: (i + 3) <= len(s)
                res.append("".join(word))
                word = []
                i = i + 3
            else:
                word.append(s[i])
                i = i + 1
        return res