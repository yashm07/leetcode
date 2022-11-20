from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        arr = [0] * len(nums)

        for k in range(0, len(nums)):
            if abs(nums[i]) >= abs(nums[j]):
                arr[len(nums)-1-k] = abs(nums[i])**2
                i += 1
            else:
                arr[len(nums)-1-k] = abs(nums[j])**2
                j -= 1
        
        return arr
                