class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # O(logn) time, O(1) space
        exp, n2 = 1, 1
        while n > n2:
            n2 += 2**exp
            exp += 1
        
        return n^n2
        