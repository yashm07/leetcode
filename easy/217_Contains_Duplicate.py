class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n) time, O(n) memory
        prev = set()

        for val in nums:
            if val in prev:
                return True
            prev.add(val)
        
        return False