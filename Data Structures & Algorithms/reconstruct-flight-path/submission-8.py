class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {src:[] for src, dest in tickets}
        for src, dest in tickets:
            adj[src].append(dest)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1: # used all tickets, +1 is for starting JFK
                return True
            if src not in adj:              # path does not exist
                return False
            
            tmp = list(adj[src])            # we modify adj list to mark edges(ticket) as used
            for i in range(len(tmp)):
                dest = tmp[i]
                res.append(dest)
                adj[src].pop(i)             # mark ticket as used
                if dfs(dest):               # find one valid path
                    return True
                adj[src].insert(i, dest)    # unmark ticket as used (backtrack)
                res.pop()                   # remove from travel history
            return False
        dfs("JFK")
        return res
                