class Solution:
    def romanToInt(self, s: str) -> int:
        # O(n) time, O(1) space
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        output = 0
        
        for i in range(len(s)-1):
            if roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                output -= roman_to_int[s[i]]
            else:
                output += roman_to_int[s[i]]
        
        return output + roman_to_int[s[-1]]
