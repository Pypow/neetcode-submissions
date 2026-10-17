class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # adj list
        adj = {c: set() for w in words for c in w}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = set()
        path = set()
        res = []
        # dfs post order traversal: reverse and return result
        def dfs(c):
            if c in path:
                return False
            if c in visit:
                return True
            path.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            visit.add(c)
            path.remove(c)
            res.append(c)
            return True

        for c in adj.keys():        # run dfs on each unique letter in words
            if not dfs(c):
                return ""
        res = reversed(res)
        return "".join(res)
