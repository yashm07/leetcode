class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(2^n) time, O(n) space
        output = []
        candidates.sort()

        def dfs(i, path):
            if sum(path) == target:
                output.append(list(path))
                return
            
            if i >= len(candidates) or sum(path) > target:
                return
            
            path.append(candidates[i])
            dfs(i+1, path)
            
            while  i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            
            path.pop()
            dfs(i+1, path)
        
        dfs(0, [])
        return output
            

      