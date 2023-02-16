class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs solution, O(n*m) time, O(n*m) space worst case due to queue and visited
        # self.count = 0
        # self.visited = set()

        # row_len, col_len = len(grid), len(grid[0])

        # def bfs(i, j):
        #     q = deque()
        #     self.visited.add((i, j))
        #     q.append((i, j))

        #     while q:
        #         row, col = q.popleft()

        #         neighbours = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

        #         for neighbour in neighbours:
        #             row, col = neighbour
        #             if row < row_len and row >= 0 and col < col_len and col >= 0 and neighbour not in self.visited and grid[row][col] == "1":
        #                 q.append((row, col))
        #                 self.visited.add((row, col))

        # for i in range(row_len):
        #     for j in range(col_len):
        #         if (i, j) not in self.visited and grid[i][j] == "1":
        #             bfs(i, j)
        #             self.count += 1
        
        # return self.count

        # recursive dfs, O(n*m) time, O(n*m) space due to call stack
        self.count = 0
        self.visited = set()

        row_len, col_len = len(grid), len(grid[0])

        def dfs(i, j):
            self.visited.add((i, j))
            neighbours = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

            for neighbour in neighbours:
                row, col = neighbour
                if row < row_len and row >= 0 and col < col_len and col >= 0 and neighbour not in self.visited and grid[row][col] == "1":
                    dfs(row, col)
                    
        for i in range(row_len):
            for j in range(col_len):
                if (i, j) not in self.visited and grid[i][j] == "1":
                    dfs(i, j)
                    self.count += 1
        
        return self.count
