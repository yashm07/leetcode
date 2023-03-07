class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memoization, O(n) time
        self.mem = {}
        def dfs(i):
            if i in self.mem: return self.mem[i]
            
            if i == len(cost):
                return 0
            
            if i > len(cost):
                return inf
            
            res = cost[i] + min(dfs(i+1), dfs(i+2))
            self.mem[i] = res
            return res
        
        return min(dfs(0), dfs(1))
        
        # bottom up approach, O(n) time
        l, r = 0, 0
        for i in range(len(cost)-1, -1, -1):
            l, r = min(cost[i]+l, cost[i]+r), l
        
        return min(l, r)