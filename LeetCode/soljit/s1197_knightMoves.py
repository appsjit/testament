class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

        queue = deque([(0, 0)])
        visited = set()
        ##queue.append((0,0))
        ##visited.add((0,0))
        steps = 0

        while queue:
            current_layer_cnt = len(queue)

            for i in range(current_layer_cnt):
                prNodeX, prNodeY = queue.popleft()

                if (prNodeX, prNodeY) == (x, y):
                    return steps
                for moveX, moveY in moves:
                    newNodeX, newNodeY = prNodeX + moveX, prNodeY + moveY
                    if (newNodeX, newNodeY) not in visited:
                        visited.add((newNodeX, newNodeY))
                        queue.append((newNodeX, newNodeY))

            steps += 1