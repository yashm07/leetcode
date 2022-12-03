# from typing import List

# # O(n) solution, uses Kadane's algorithm
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         overall_sum = nums[0]
#         cur_sum = 0

#         for n in nums:
#             if cur_sum < 0:
#                 cur_sum = 0
#             cur_sum += n
#             overall_sum = max(cur_sum, overall_sum)
    
#         return overall_sum


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         local_max = 0
#         global_max = -inf

#         for i in range(0, len(nums)):
#             local_max = max(nums[i], nums[i] + local_max)
#             global_max = max(local_max, global_max)
        
#         return global_max

class Solution:
    def insert(self, intervals, newInterval):
        output = []

        for i in range(len(intervals)):
            # if self.overlap(intervals[i][0], intervals[i][1], newInterval[0], newInterval[1]):
            # if self.overlap(intervals[i][0], intervals[i][1], newInterval[0], newInterval[1]):
            val1 = intervals[i][0]
            val2 = intervals[i][1]
            val3 = newInterval[0]
            val4 = newInterval[1]
            if self.overlap(val1, val2, val3, val4):
                output.append([min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])])
                j += 1
                
                while self.overlap(intervals[j][0], intervals[j][1], output[-1][0], output[-1][1]):
                    output[-1][0] = min(output[-1][0], intervals[j][0])
                    output[-1][1] = min(output[-1][1], intervals[j][1])
        
        output.append(intervals[j:])
        
        return output
    
    def overlap(min1, max1, min2, max2):
        if max1 < min2 or min1 > max2:
            return False
        return True
dm = Solution()
dm.insert([[1,3],[4,6]], [6,7])