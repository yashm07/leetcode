class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        window_dict = {}
        start = 0

        for end in range(0, len(s)):
            while s[end] in window_dict:
                    window_dict.pop(s[start])
                    start += 1
            
            max_length = max(max_length, end-start+1)
            window_dict[s[end]] = 0
        
                
        
        return max_length
