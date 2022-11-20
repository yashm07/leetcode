from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.binarySearch(nums, target, True)
        r = self.binarySearch(nums, target, False)
        
        return [l, r]
    
        
    
    def binarySearch(self, nums, target, left_index):
        l = 0
        r = len(nums) - 1
        i = -1
        
        while l <= r:
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                i = mid
                
                if left_index:
                    r = mid - 1
                else:
                    l = mid + 1
            
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return i
                