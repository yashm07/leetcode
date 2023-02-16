class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = 0
        second = cost[-1]

        for i in range(len(cost)-2, -1, -1):
            min_cost = min(first, second)
            second, first = min_cost+cost[i], second
            
        return min(first, second)