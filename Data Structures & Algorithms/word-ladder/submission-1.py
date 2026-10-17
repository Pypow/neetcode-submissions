class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        visit = set()
        adj = defaultdict(list)
        wordList.append(beginWord)
        q = deque()
        q.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj[pattern].append(word)

        count = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            count += 1 
        return 0 

                

