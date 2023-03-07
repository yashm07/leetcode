class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2) time, O(1) space
        output, output_len = "", 0

        for i in range(len(s)):
            start, end = i, i
            output, output_len = self.isPalindrome(start, end, s, output, output_len)
        
        for i in range(len(s)):
            start, end = i, i+1
            output, output_len = self.isPalindrome(start, end, s, output, output_len)
        
        return output
                    
    def isPalindrome(self, start, end, s, output, output_len):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            if end-start+1 > output_len:
                output = s[start:end+1]
                output_len = end-start+1
            
            start -= 1
            end += 1
        
        return output, output_len
        