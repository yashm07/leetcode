class Solution:
    def climbStairs(self, n: int) -> int:
        # memoization, O(n) time
        # self.mem = {}
        # def dfs(i):
        #     if i in self.mem: return self.mem[i]
        #     if i > n:
        #         return 0
            
        #     if i == n:
        #         return 1
            
        #     res = dfs(i+1) + dfs(i+2)
        #     self.mem[i] = res
        #     return res
        
        # return dfs(0)

        # bottom up approach - fibonacci sequence, O(n) time
        if n <= 2:
            return n
        
        l, r = 1, 1
        
        for _ in range(n-1):
            tmp = r
            r = l+r
            l = tmp
        
        return r
        