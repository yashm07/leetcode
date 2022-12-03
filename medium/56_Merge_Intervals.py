class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastMin = output[-1][0]
            lastMax = output[-1][1]
            if self.overlap(lastMin, lastMax, start, end):
                output[-1][1] = max(lastMax, end)
            else:
                output.append([start, end])
        
        return output
        
        
        # intervals.sort(key=lambda x: x[0])

        # output = []
        # curIntervalMin = intervals[0][0]
        # curIntervalMax = intervals[0][1]

        # for i in range(1, len(intervals)):
        #     if self.overlap(curIntervalMin, curIntervalMax, intervals[i][0], intervals[i][1]):
        #         curIntervalMax = max(curIntervalMax, intervals[i][1])
        #     else:
        #         output.append([curIntervalMin, curIntervalMax])
        #         curIntervalMin = intervals[i][0]
        #         curIntervalMax = intervals[i][1]
        
        # output.append([curIntervalMin, curIntervalMax])

        # return output
    
    def overlap(self, min1, max1, min2, max2):
        if min1 > max2 or max1 < min2:
            return False
        return True
            
        
    
    
    
    
    
    
    
    
    