class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # very interesting approach
        # since sorted list, use binary search
        # combines idea with cyclic sort and using the index positions to tell how many
        # missing integers so far
        # O(log n) time complexity, O(1) space complexity
        l, r = 0, len(arr)-1

        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] - (mid+1) < k:
                l = mid + 1
            else:
                r = mid -1
        
        return l+k
