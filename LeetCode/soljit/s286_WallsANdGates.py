#import Queue


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # def checker(pr, pc):
        #     ## Checking Boundaries
        #     if (pr >= 0 and pr < len(rooms) and pc >= 0 and pc < len(rooms[0])):

        if not rooms or not rooms[0]:
            return

        myQueue = Queue.Queue()

        disha = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        nr = len(rooms)
        nc = len(rooms[0])

        curcell = -1
        for r in range(len(rooms)):
            for c in range(len(rooms[r])):
                if (rooms[r][c] == 0):  ##  Start from Gate
                    myQueue.put([r, c])

        while not myQueue.empty():  ## Breadth First Search to start updating adjacent
            curcell = myQueue.get()
            curRo = curcell[0]
            curCo = curcell[1]
            for d in disha:
                r = curRo + d[0]
                c = curCo + d[1]

                if 0 <= r < nr and 0 <= c < nc and rooms[r][c] == 2 ** 31 - 1:
                    rooms[r][c] = rooms[curRo][curCo] + 1
                    myQueue.put([r, c])


