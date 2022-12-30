class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        i, j = 0, 0
        output = []

        def dfs(i, j, path):
            if i == j == n:
                output.append("".join(path))
                return
            
            if i < n:
                path.append("(")
                dfs(i+1, j, path)
                path.pop()
            
            if i != j:
                path.append(")")
                dfs(i, j+1, path)
                path.pop()
         
        dfs(0, 0, [])
        return output
        

            

            
            
