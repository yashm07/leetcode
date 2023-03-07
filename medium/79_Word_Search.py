class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # O(n*m*4^n) time - backtracking solution
        rows, cols = len(board), len(board[0])
        path = set()
        def dfs(i, j, k):
            if k == len(word): return True
            if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in path or board[i][j] != word[k]: return False

            path.add((i, j))
            res = True if dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1) else False
            path.remove((i, j))
            return res


        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0): return True
        
        return False