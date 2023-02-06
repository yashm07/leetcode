class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) time, O(n) memory
        counts = Counter(s)

        for i in range(len(t)):
            if t[i] in counts and counts[t[i]] > 0:
                counts[t[i]] -= 1
            else:
                return False
        
        return len(s) == len(t)
