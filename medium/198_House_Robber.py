class Solution:
    # brute force, 2^n
    # def rob(self, nums: List[int]) -> int:
    #     self.output = 0

    #     def dfs(i, cur_sum):
    #         if i >=0 and i < len(nums): cur_sum += nums[i]
            
    #         if i+2 >= len(nums):
    #             self.output = max(self.output, cur_sum)
    #             return
            
            
    #         dfs(i+2, cur_sum)
    #         dfs(i+3, cur_sum)
        
    #     dfs(-2, 0)
    #     return self.output

    # recurrence relation (seeing the subproblem) with memoization
    # def rob(self, nums: List[int]) -> int:
    #     mem = {}
    #     def dfs(i):
    #         if i < 0:
    #             return 0
            
    #         if i in mem: return mem[i]
            
    #         res = max(nums[i] + dfs(i-2), dfs(i-1))
    #         mem[i] = res
    #         return res
        
    #     return dfs(len(nums)-1)

    # bottom up approach, best approach
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, nums[0]

        for i in range(1, len(nums)): 
            prev, curr = curr, max(prev + nums[i], curr)
        
        return curr

