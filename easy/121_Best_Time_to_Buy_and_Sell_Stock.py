class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) time, O(1) space
        l, output = 0, 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                output = max(output, prices[r]-prices[l])
        
        return output
                        
