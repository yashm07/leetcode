class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # trickier solution, O(n) time, O(1) space
        output = max(nums)
        cur_max, cur_min = 1, 1

        for num in nums:
            if num == 0:
                cur_min, cur_max = 1, 1
            else:
                tmp = num*cur_max
                cur_max = max(num*cur_max, num*cur_min, num)
                cur_min = min(tmp, num*cur_min, num)
                output = max(cur_max, output)
        
        return output
            