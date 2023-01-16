class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # solution I came up with, does not follow division rule but still O(n) time and O(1) space
        # total_product = 1
        # seen_zero, index_zero = False, 0
        # output = [0] * len(nums)
        
        # for i in range(len(nums)):
        #     if nums[i] == 0 and not seen_zero:
        #         seen_zero = True
        #         index_zero = i
        #     elif nums[i] == 0 and seen_zero:
        #         return output
        #     else:
        #         total_product *= nums[i]
        
        # if seen_zero:
        #     output[index_zero] = total_product
        #     return output
        
        # for i in range(len(nums)):
        #     output[i] = int(total_product/nums[i])
        
        # return output

        # uses prefix and postfix method, O(n) time, O(1) space
        output = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]
        
        return output

        # in one loop, same solution as above
        # prefix, postfix = 1, 1
        # i, j = 0, len(nums)-1
        # while i < len(nums):
        #     if i < j:
        #         output[i] = prefix
        #         output[j] = postfix
        #     else:
        #         output[i] *= prefix
        #         output[j] *= postfix
        #     prefix *= nums[i]
        #     postfix *= nums[j]
        #     i += 1
        #     j -= 1
        
        # return output
        
        
