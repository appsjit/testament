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


    def minMeetingRoomsPointers(self, intervals: List[List[int]]) -> int:
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0
        #         q = []
        intervals.sort(key=lambda x: x[0])

        no_of_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        startTime = sorted(i[0] for i in intervals)
        endTime = sorted(i[1] for i in intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        startPointer, endPointer = 0, 0
        while startPointer < len(intervals):
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if startTime[startPointer] >= endTime[endPointer]:
                # Free up a room and increment the end_pointer.
                no_of_rooms -= 1
                endPointer += 1

            startPointer += 1
            no_of_rooms += 1

        return no_of_rooms

#         heapq.heappush(q, intervals[0][1])
#         for i in intervals[1:]:

#             if q[0] <= i[0]:
#                 heapq.heappop(q)
#             heapq.heappush(q, i[1])

#         print(len(q))

#         return len(q)


