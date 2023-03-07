class Solution:
    def rob(self, nums: List[int]) -> int:
        self.mem = {}
        
        
        def dfs(nums1):
            left, right = 0, 0

            for i in range(len(nums1)):
                right, left = max(nums1[i] + left, right), right

            return right
        
        return max(dfs(nums[1:]), dfs(nums[:-1])) if len(nums) != 1 else nums[0]
        

        