class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # O(n*m) time, O(n*m) worst space
        rows, cols = len(heights), len(heights[0])
        p, a = set(), set()

        def dfs(i, j, visited, prev_height):
            if i < 0 or i >= rows or j < 0 or j >= cols or heights[i][j] < prev_height or (i, j) in visited:
                return
            
            visited.add((i, j))
            directions = [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]

            for x, y in directions: dfs(x, y, visited, heights[i][j])
        
        for c in range(cols):
            dfs(0, c, p, heights[0][c])
            dfs(rows-1, c, a, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, p, heights[r][0])
            dfs(r, cols-1, a, heights[r][cols-1])
        
        output = []
        for set1 in p:
            for set2 in a:
                if set1 == set2:
                    output.append(set1)
                    break
        
        return output
        # return list(p.intersection(a))