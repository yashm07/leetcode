# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         # All solutions are O(n) runtime and O(1) space complexity
#         # # cylic sort approach 
#         # start = 0
#         # while start < len(nums):
#         #     if nums[start] < len(nums) and nums[start] != start:
#         #         nums[nums[start]], nums[start] = nums[start], nums[nums[start]]
#         #     else:
#         #         start += 1
        
#         # for i in range(len(nums)):
#         #     if nums[i] != i:
#         #         return i
        
#         # return len(nums)

#         # # sum approach
#         # output = len(nums)
#         # for i in range(len(nums)):
#         #     output += (i - nums[i])
#         # return output

#         # bit manipulation approach - XOR
#         result = len(nums)
#         for i, val in enumerate(nums):
#             result ^= i
#             result ^= val
        
#         return result
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        start = 0
        while start < len(nums):
            if nums[start] != start+1 and nums[start] != nums[nums[start]-1]:
                print(nums[start])
                print(nums[nums[start]-1])
                nums[nums[start]-1], nums[start] = nums[start], nums[nums[start]-1]
                print("here")
            else:
                start += 1
               
        
        for i in range(len(nums)):
            if i+1 != nums[i]:
                output.append(nums[i])
        
        return output
sol = Solution()
sol.findDisappearedNumbers(nums=[4,3,2,7,8,2,3,1])