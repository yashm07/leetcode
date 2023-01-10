class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # O(nlogn) time, O(k) memory
        self.heap = nums[:min(k, len(nums))]
        self.k = k
        heapify(self.heap)
        
        for i in range(k, len(nums)):
            if nums[i] > self.heap[0]:
                heappushpop(self.heap, nums[i])
        
    def add(self, val: int) -> int:
        # O(logn) time, O(1) memory
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        
        return self.heap[0] 


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)