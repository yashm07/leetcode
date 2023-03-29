class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # O(n^2*m approach)
        # if endWord not in wordList: return 0
        
        # # creates graph
        # graph = {}
        # wordList.append(beginWord)
        # for w in wordList:
        #     for w2 in wordList:
        #         if w not in graph: graph[w] = []
        #         if w == w2: continue

        #         diff = 0
        #         for i in range(len(w)):
        #             if w[i] != w2[i]: diff += 1
                
        #         if diff == 1:
        #             graph[w].append(w2)
        
        # # bfs
        # q = deque()
        # visited = set()
        
        # q.append(beginWord)
        # visited.add(beginWord)
        # res = 1

        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()

        #         if node == endWord: return res
                
        #         for n in graph[node]:
        #             if n not in visited:
        #                 q.append(n)
        #                 visited.add(n)
                
        #     res += 1
        
        # return 0

        # also O(n^2m) time, but slightly more efficient as O(n*m^2) time for creating graph
        if endWord not in wordList: return 0

        wordList.append(beginWord)
        graph = {}

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                if pattern not in graph: graph[pattern] = []
                graph[pattern].append(word)
            
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node == endWord: return res

                for j in range(len(node)):
                    pattern = node[:j] + "*" + node[j+1:]

                    for n in graph[pattern]:
                        if n not in visited:
                            q.append(n)
                            visited.add(n)
            
            res += 1

        return 0


