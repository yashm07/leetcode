from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        window_sum = 0
        min_length = inf

        for end in range(0, len(nums)):
            window_sum += nums[end]

            while (window_sum >= target):
                min_length = min(min_length, end-start+1)
                window_sum -= nums[start]
                start += 1
        
        return 0 if min_length == inf else min_length