class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # O(n4^n) time complexity, O(n) space
        num_let = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        output = []

        def dfs(i, cur_str):
            if not digits: return output
            
            if i == len(digits):
                output.append(cur_str)
                return
            
            for j in num_let[digits[i]]:
                dfs(i+1, cur_str + j)
        
        dfs(0, "")
        return output