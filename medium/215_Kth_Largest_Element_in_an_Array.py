class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # solution using min_heap
        # O(nlogk) time, O(k) memory
        # min_heap = []

        # for i in range(k):
        #     heappush(min_heap, nums[i])
        
        # for i in range(k, len(nums)):
        #     if nums[i] > min_heap[0]:
        #         heappop(min_heap)
        #         heappush(min_heap, nums[i])
        
        # return min_heap[0]

        # another heap solution - more inefficient
        # nums_heap = [-1 * i for i in nums]
        # heapify(nums_heap)
        
        # for i in range(k-1):
        #     heappop(nums_heap)
        
        # return -1 * nums_heap[0]

        # using quick select - algorithm designed for literally this problem
        # O(n) average case, O(n^2) worst case
        k = len(nums)-k

        def quickSelect(l, r):
            pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]

            if k == i:
                return nums[i]
            elif k > i:
                return quickSelect(i+1, r)
            else:
                return quickSelect(l, i-1)
        
        return quickSelect(0, len(nums)-1)



        