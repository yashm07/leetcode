class Solution:
    def countSubstrings(self, s: str) -> int:
        # O(n^2) time, O(1) space
        output = 0
        
        for i in range(len(s)):
           output = self.checkPalindrome(i, i, s, output)
           output = self.checkPalindrome(i, i+1, s, output)

        return output
        
    def checkPalindrome(self, l, r, s, output):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            output += 1
            l -= 1
            r += 1
        
        return output
