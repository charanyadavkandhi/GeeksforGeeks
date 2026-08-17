from collections import deque

class Solution:
    def minThrows(self, n, ladders, snakes):
        size = n * n

        # Store snakes and ladders
        jump = {}

        for i in range(0, len(ladders), 2):
            jump[ladders[i]] = ladders[i + 1]

        for i in range(0, len(snakes), 2):
            jump[snakes[i]] = snakes[i + 1]

        # BFS
        queue = deque()
        queue.append((1, 0))

        visited = [False] * (size + 1)
        visited[1] = True

        while queue:
            cell, throws = queue.popleft()

            # Reached destination
            if cell == size:
                return throws

            # Try dice values 1 to 6
            for dice in range(1, 7):
                next_cell = cell + dice

                if next_cell > size:
                    continue

                # Snake or ladder
                if next_cell in jump:
                    next_cell = jump[next_cell]

                if not visited[next_cell]:
                    visited[next_cell] = True
                    queue.append((next_cell, throws + 1))

        return -1