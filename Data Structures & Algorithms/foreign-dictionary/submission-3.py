class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        # build adj list
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w2[:minLen] == w1[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        # post order traversal   
        visit = {}  # False: Visited, # True: visiting
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:  
                if dfs(nei):    # cycle detection
                    return True
            visit[c] = False
            res.append(c)
        
        for c in adj.keys():
            if dfs(c):
                return ""
        return "".join(reversed(res))
            