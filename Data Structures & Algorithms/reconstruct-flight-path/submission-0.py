class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src:[] for src, des in tickets}
        tickets.sort()

        for src, dest in tickets:
            adj[src].append(dest)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            tmp = list(adj[src])
            for i, v in enumerate(tmp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)           # backtrack if dfs(v) == False
                res.pop()
            return False
        dfs("JFK")
        return res

