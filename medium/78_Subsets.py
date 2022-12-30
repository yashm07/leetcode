class Solution:
    # dfs approach, uses backtracking and recursion
    # O(n2^n) time complexity due to copying, O(n) space complexity
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        path = []
        
        def dfs(i):
            if i == len(nums):
                output.append(list(path))
                return

            path.append(nums[i])
            dfs(i+1)
            path.pop()
            dfs(i+1)
        
        dfs(0)
        return output

   