class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # O(n)
        i = 0
        output = []
        while i < len(nums):
            correct_index = nums[i]-1
            if nums[i] != correct_index and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        
        for i, val in enumerate(nums):
            if val != i+1:
                output.append(val)
        
        return output
        