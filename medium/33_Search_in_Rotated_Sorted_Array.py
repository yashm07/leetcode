from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid
            
            # if the middle is a part of the left sublist, e.g. 3,4,5,6,1,2
            elif nums[mid] > nums[r]:
                if (target > nums[mid] or target <= nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1
            
            # if the middle is a part of the right sublist, e.g. 1,2,3,4,5,6
            else:
                if (target > nums[mid] and target <= nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1 

