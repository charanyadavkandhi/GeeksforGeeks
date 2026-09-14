from collections import deque

class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        # safe[i][j] = True if the cell can be used
        safe = [[True] * m for _ in range(n)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Mark landmines and their adjacent cells as unsafe
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    safe[i][j] = False

                    for di, dj in directions:
                        ni = i + di
                        nj = j + dj

                        if 0 <= ni < n and 0 <= nj < m:
                            safe[ni][nj] = False

        # BFS
        q = deque()
        dist = [[-1] * m for _ in range(n)]

        # Start from every safe cell in the first column
        for i in range(n):
            if safe[i][0]:
                q.append((i, 0))
                dist[i][0] = 1

        while q:
            i, j = q.popleft()

            # Reached the last column
            if j == m - 1:
                return dist[i][j]

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (0 <= ni < n and
                    0 <= nj < m and
                    safe[ni][nj] and
                    dist[ni][nj] == -1):

                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))

        return -1