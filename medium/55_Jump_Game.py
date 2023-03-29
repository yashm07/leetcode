class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dynamic programming approach, bottom-up, O(n^2) time due to nested loops
        # arr = [False] * len(nums)
        # arr[-1] = True

        # for i in range(len(nums)-2, -1, -1):
        #     for j in range(nums[i], 0, -1):                
        #         if i+j < len(nums) and arr[i+j]: 
        #             arr[i] = True
        #             break
            
        # return arr[0]
        
        # greedy approach, O(n) time
        end = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= end:
                end = i
        
        return True if end == 0 else False