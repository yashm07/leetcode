class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(klogn) (assuming entire heap is heapified O(n) then popped k times klogn) time, O(n+k) memory (n for hashmap, worst case all elements are unique, k for heap)
        # solution says O(nlogk), which means that heap is k size and iterates through all elements to get top k elements
        # generate dictionary of unique num counts
        # counts = Counter(nums)
        # # use heap and sort by dict values, and get n largest elements 
        # # this function works with iterables
        # return heapq.nlargest(k, counts.keys(), key=counts.get)

        # bucket sort approach, O(n) time, O(n) memory
        # interesting way - creates hashmap of count, then uses freq array (index represents count, and values represent the nums with that count)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        output = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output
        


        

        