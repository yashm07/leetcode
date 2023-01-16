class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # bit manipulation
        # O(n) time, O(1) memory
        num = 0
        for i in nums:
            num ^= i
        return num