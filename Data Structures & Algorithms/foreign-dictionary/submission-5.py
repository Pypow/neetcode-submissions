class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # two set() to visit and cycle
        adj = {c: set() for w in words for c in w}   # set to avoid duplicates

        # Adj list
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visited = set()
        path = set()
        res = []
        # graph traversal: post order DFS and reverse the res

        def dfs(c):
            if c in path:          # contains cycle
                return False
            if c in visited:          
                return True        # already visited
            path.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            path.remove(c)
            visited.add(c)
            res.append(c)          # post order DFS
            return True            # successfully traversed the graph
        
        for c in adj.keys():
            if not dfs(c):
                return ""
        res.reverse()
        return "".join(res)
            