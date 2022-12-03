class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # cyclic approach, O(n) run time, O(1) memory 
        i = 0
        while i < len(nums):
            correct_index = nums[i]-1
            # check if value would fit in array
            # check if duplicate
            # check if value is in right spot
            # check if value is positive
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != i+1 and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        
        for i, val in enumerate(nums):
            if val != i+1:
                return i+1
        
        return len(nums)+1