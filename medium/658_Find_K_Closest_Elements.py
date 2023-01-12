class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # O(nlogk) time, O(k) or O(n) depending if output counts for memory
        min_heap = []

        for i in range(0, k):
            heappush(min_heap, arr[i])
        
        for i in range(k, len(arr)):
            # if a smaller distance is found, that means the smallest value in the heap is the further - key pattern in this solution
            if abs(arr[i] - x) < abs(min_heap[0] - x):
                heappop(min_heap)
                heappush(min_heap, arr[i])
                # heappushpop(min_heap, arr[i])
    
        output = []
        while min_heap:
            output.append(heappop(min_heap))
        
        return output



