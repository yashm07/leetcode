class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # O(n2^n solution) due to copying of list, very similar to other subsets problem, dfs approach
        # O(n) memory due to calls stack
        output = []
        path = []

        def dfs(i):
            if i == len(nums):
                output.append(list(path))
                return
            
            path.append(nums[i])
            dfs(i+1)

            path.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            dfs(i+1)
        
        dfs(0)
        return output
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # bfs approach
        output = [[]]
        nums.sort()

        for j, num in enumerate(nums):
            if j > 0 and nums[j] == nums[j-1]:
                start += count
            else:
                start = 0
            count = 0
            for i in range(start, len(output)):
                output.append(output[i] + [num])
                count += 1
        
        return output

                

       