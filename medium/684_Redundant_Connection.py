class Solution(object):
    def findRedundantConnection(self, edges):
        # brute force method, O(n^2) time   
        # graph = {}

        # def dfs(source, target):
        #     if source not in seen:
        #         seen.add(source)
        #         if source == target: return True

        #         for n in graph[source]:
        #             if dfs(n, target): return True
                
        #         return False

        # for u, v in edges:
        #     seen = set()
        #     if u in graph and v in graph and dfs(u, v): return u, v

        #     if u not in graph: graph[u] = []
        #     if v not in graph: graph[v] = []
        #     graph[u].append(v)
        #     graph[v].append(u)
        
        # union find
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]

            while p != par[p]:
                # compression technique
                par[p] = par[par[p]]
                p = par[p]

            return p
        
        def union(u, v):
            # find root parents
            p1, p2 = find(u), find(v)

            # part of same subset
            if p1 == p2: return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for u, v in edges:
            if not union(u, v): return [u, v]