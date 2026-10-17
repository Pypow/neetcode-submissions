class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        res = []
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord("a")] += 1
            key = tuple(key)
            if key not in hmap:
                hmap[key] = []
            hmap[key].append(word)
        
        for val in hmap.values():
            res.append(val)
        return res
