class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)

        while l < r:
            mid = l + (r-l)//2

            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1
            
        if r >= len(letters):
            return letters[0]
        
        return letters[r]
            