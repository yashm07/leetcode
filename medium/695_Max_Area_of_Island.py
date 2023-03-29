class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs approach
        # O(n*m*4^n) time, O(n*m) worst space
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            output = 0
            
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or (i, j) in visited:
                return output
            
            directions = [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]
            visited.add((i, j))

            for x, y in directions:
                output += dfs(x, y)
            
            return output+1
        
        res = 0
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        return res
            