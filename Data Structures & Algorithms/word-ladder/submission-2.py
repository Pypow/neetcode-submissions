class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj = collections.defaultdict(list)
        res = 1
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)
        
        visit = set()
        q = collections.deque()
        q.append(beginWord)
        visit.add(beginWord)

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in adj[pattern]:
                        if nei in visit:
                            continue
                        visit.add(nei)
                        q.append(nei)
            res += 1
        return 0
            
