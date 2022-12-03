class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # cylic approach, O(n) run time and O(1) memory, however, modifies the original nums
        # i = 0
        # correct_index = nums[i]
        # while nums[i] != nums[correct_index]:    
        #     nums[i], nums[correct_index] = nums[correct_index], nums[i]
        #     correct_index = nums[i]
        # return nums[i]

        # uses floyd's algorithm, didn't spend too much time here, go over solution
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
            