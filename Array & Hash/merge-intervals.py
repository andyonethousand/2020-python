class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        
        if len(intervals) == 1:
            return [intervals[0]]
        
        response = []
        
        intervals.sort(key = lambda x: x[0])
        
        for i in intervals:
            if len(response) == 0 or response[-1][1] < i[0]:
                response.append(i)
            else:
                response[-1][1] = max(response[-1][1], i[1])
        
        return response
