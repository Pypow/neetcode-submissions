class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)   # [0*26]: list of common strs
        for s in strs:
            a = [0]*26
            for c in s:
                i = ord(c) - ord('a')
                a[i] += 1
            hmap[tuple(a)].append(s)
        return hmap.values()