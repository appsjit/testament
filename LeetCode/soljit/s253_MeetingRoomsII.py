import heapq
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        avRooms = []
        intervals.sort(key=lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(avRooms, intervals[0][1])

        # For all the remaining meeting rooms
        for x in intervals[1:]:
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if avRooms[0] <= x[0]:
                heapq.heappop(avRooms)
            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(avRooms, x[1])

        return len(avRooms)

