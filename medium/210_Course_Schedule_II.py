class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # O(n+e) time, O(n) space 
        # topological sort, dfs
        adjList = {i: [] for i in range(numCourses)}

        for i, j in prerequisites:
            adjList[j].append(i)
        
        visited = set()
        globalVisited = set()
        output = deque()

        def dfs(node):
            if node in visited: return False
            if node in globalVisited: return True

            visited.add(node)
            globalVisited.add(node)

            for n in adjList[node]:
                if not dfs(n): return False
            
            visited.remove(node)
            output.appendleft(node)
            return True
        
        for node in adjList:
            if not dfs(node): return []
        
        return output
