class Solution:
    def isPalindrome(self, s: str) -> bool:
        # instead of using isalnum, create own method that uses ord to check
        # O(n) time, O(1) space
        l, r = 0, len(s)-1

        while l < r:
            # check if invalid
            while l < len(s) and not s[l].isalnum() :
                l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1

            if r >= 0 and l < len(s):
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
         
        return True