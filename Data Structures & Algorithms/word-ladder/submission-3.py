class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj = defaultdict(list)
        wordList.append(beginWord)  # include beginWord
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)
        
        visit = set()
        q = collections.deque()
        q.append(beginWord)
        visit.add(beginWord)
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in adj[pattern]:
                        if neiWord not in visit:
                            q.append(neiWord)
                            visit.add(neiWord)
            res += 1
        return 0










