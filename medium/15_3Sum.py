from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l,r = i+1, len(nums)-1

            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]

                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
        return output