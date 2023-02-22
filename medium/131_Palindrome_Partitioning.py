class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path, output = [], []

        def dfs(i):
            if i == len(s):
                output.append(list(path))
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
        
        dfs(0)
        return output
        
    
    def isPalindrome(self, word):
        return True if word == word[::-1] else False
        