class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        available_rooms = []
                
        intervals.sort(key = lambda x: x[0])
        
        heapq.heappush(available_rooms, intervals[0][1])
        
        for i in intervals[1:]:
            if available_rooms[0] <= i[0]:
                heapq.heappop(available_rooms)
                
            heapq.heappush(available_rooms, i[1])
        
        return len(available_rooms)
