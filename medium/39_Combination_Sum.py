class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # dfs approach
        # O(2^target), each node there are 2 decisions and at most target levels
        # O(n) memory due to path
        output = []

        def dfs(i, path, cur_sum):
            if cur_sum == target:
                output.append(list(path))
                return
            
            elif i >= len(candidates) or cur_sum > target:
                return
            
            path.append(candidates[i])
            dfs(i, path, cur_sum + candidates[i])
            path.pop()
            dfs(i+1, path, cur_sum)
        
        dfs(0, [], 0)
        return output