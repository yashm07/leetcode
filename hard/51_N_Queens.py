class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # potentially O(n!) time complexity, O(n) space
        cols = set()
        posDiag = set() # r + c
        negDiag = set() # r - c

        output = []
        board = [["."] * n for _ in range(n)]
        
        def dfs(r):
            if r == n:
                copy = ["".join(board[i]) for i in range(n)]
                output.append(copy)
                return
            
            for c in range(n):
                if c in cols or r+c in posDiag or r-c in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                dfs(r+1)

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        dfs(0)
        return output