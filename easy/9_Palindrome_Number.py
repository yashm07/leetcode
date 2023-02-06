class Solution:
    def isPalindrome(self, x: int) -> bool:
        # method 1: reverse the number
        # if x < 0:
        #     return False
        
        # num = x
        # reversed_num = 0

        # while x:
        #     right_digit = x % 10 
        #     reversed_num = reversed_num * 10 + right_digit
        #     x //= 10
        
        # return reversed_num == num

        # method 2: "two pointers" in a way
        if x < 0: return False
        
        div, i = 1, 1
        while x // i > 0:
            div = i
            i *= 10

        while x:
            r_digit = x % 10
            l_digit = x // div

            if r_digit != l_digit:
                return False
            
            x = (x % div) // 10

            div //= 100
        
        return True