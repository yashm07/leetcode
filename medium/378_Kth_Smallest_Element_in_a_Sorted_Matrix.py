class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # solved using merge k sorted lists pattern
        # O(klogk) time, O(k) space
        min_heap = []

        for i, l in enumerate(matrix):
            heappush(min_heap, (l[0], i, 0))
        
        for _ in range(k):
            val, level, index = heappop(min_heap)
            if index + 1 < len(matrix[level]):
                heappush(min_heap, (matrix[level][index+1], level, index+1))
                
        return val
                
