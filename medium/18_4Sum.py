class Solution:
    # recursive solution for k sum
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output, quad = [], []
        nums.sort()
        size = len(nums)

        def kSum(k: int, start: int, target: int):
            if k != 2:
                for i in range(start, size+1-k):
                    if i > start and nums[i] == nums[i-1]:
                        continue

                    quad.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    quad.pop()
                return
            
            l = start
            r = size-1

            while l < r:
                current_sum = nums[l] + nums[r]
                if current_sum > target:
                    r -= 1
                elif current_sum < target:
                    l += 1
                else:
                    output.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
        kSum(4, 0, target)
        return output
                





        # iterative solution for 4 only
        # output = []
        # nums.sort()
        # size = len(nums)

        # for i in range(0, size-3):
        #     if i > 0 and nums[i-1] == nums[i]:
        #         continue
            
        #     for j in range(i+1, size-2):
        #         if j > i+1 and nums[j-1] == nums[j]:
        #             continue

        #         l = j+1
        #         r = size-1

        #         while l < r:
        #             current_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    
        #             if current_sum > target:
        #                 r -= 1
        #             elif current_sum < target:
        #                 l += 1
        #             else:
        #                 output.append([nums[i], nums[j], nums[l], nums[r]])
        #                 l += 1
        #                 while l < r and nums[l] == nums[l-1]:
        #                     l += 1
        
        # return output