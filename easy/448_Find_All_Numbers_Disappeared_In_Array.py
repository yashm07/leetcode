class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # O(n) cylic sort approach, O(1) memory
        # use cyclic sort when array in range [1,n]
        start = 0
        output = []
        while start < len(nums):
            correct_index = nums[start]-1
            if nums[start] != correct_index and nums[start] != nums[correct_index]:
                nums[start], nums[correct_index] = nums[correct_index], nums[start]
            else:
                start += 1
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                output.append(i+1)
        
        return output
        