from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = 0
        global_max = -inf

        for i in range(0, len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            global_max = max(local_max, global_max)
        
        return global_max