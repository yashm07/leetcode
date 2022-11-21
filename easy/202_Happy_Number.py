class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.getSum(n)

        while fast != 1 and slow != fast:
            slow = self.getSum(slow)
            fast = self.getSum(self.getSum(fast))
            
        return fast == 1
        
    def getSum(self, n: int) -> int:
        nums = list(str(n))
        curSum = 0
        for num in nums:
            curSum += int(num)**2
        
        return curSum
    