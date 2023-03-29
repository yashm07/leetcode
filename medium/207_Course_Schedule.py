class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs method, solve using bfs as well
        # O(n+p) (nodes+edges) time, O(n) space
        adjList = {i: [] for i in range(numCourses)}

        for i, j in prerequisites:
            adjList[i].append(j)

        pathVisited = set()

        def dfs(i):
            if i in pathVisited: return False
            if adjList[i] == []: return True
            
            pathVisited.add(i)

            for n in adjList[i]:
                if not dfs(n): return False
        
            pathVisited.remove(i)    
            adjList[i] = []
            
            return True

        for node in adjList:
            if not dfs(node): return False
        
        return True
        