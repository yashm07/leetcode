class Solution:
    def climbStairs(self, n: int) -> int:
        # brute force, O(2^n) time
        # self.output = 0
        
        # def dfs(cur_sum):
        #     if cur_sum == n:
        #         self.output += 1
        #         return
            
        #     if cur_sum + 1 <= n: dfs(cur_sum+1)
        #     if cur_sum + 2 <= n: dfs(cur_sum+2)
        
        # dfs(0)
        # return self.output

        # memoization, O(n) time
        # self.dict = {}
        
        # def dfs(cur_sum):
        #     if cur_sum == n:
        #         return 1
        #     if cur_sum > n:
        #         return 0
        #     if cur_sum in self.dict:
        #         return self.dict[cur_sum]

        #     total = dfs(cur_sum+1) + dfs(cur_sum+2)
        #     self.dict[cur_sum] = total
        #     return total
        
        # return dfs(0)

        # tabluation, bottom-up approach, best solution
        first, second = 1, 1
        for _ in range(n-1):
            first, second = second, first+second
        
        return second

