class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # dfs solution
        # O(n*n!) time complexity as n! outcomes and each outcome is length n
        # O(n) space complexity
        output = []

        def dfs(path):
            if len(path) == len(nums):
                output.append(list(path))
                return
            
            for i, val in enumerate(nums):
                if val in path: continue
                path.append(val)
                dfs(path)
                path.pop()
        
        dfs([])
        return output