class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = inf
        output = []

        # find min difference
        for i in range(len(arr)-1):
            min_diff = min(arr[i+1] - arr[i], min_diff)
        
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == min_diff:
                output.append([arr[i], arr[i+1]])
        
        return output
            
