from collections import deque

class Solution:
    def countCoordinates(self, mat):
        n = len(mat)
        m = len(mat[0])

        def bfs(starts):
            vis = [[False] * m for _ in range(n)]
            q = deque()

            for r, c in starts:
                if not vis[r][c]:
                    vis[r][c] = True
                    q.append((r, c))

            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < n and 0 <= nc < m and
                        not vis[nr][nc] and
                        mat[nr][nc] >= mat[r][c]):
                        vis[nr][nc] = True
                        q.append((nr, nc))
            return vis

        # Station P: top row + left column
        p_starts = [(0, j) for j in range(m)] + [(i, 0) for i in range(n)]

        # Station Q: bottom row + right column
        q_starts = [(n - 1, j) for j in range(m)] + [(i, m - 1) for i in range(n)]

        p_vis = bfs(p_starts)
        q_vis = bfs(q_starts)

        ans = 0
        for i in range(n):
            for j in range(m):
                if p_vis[i][j] and q_vis[i][j]:
                    ans += 1

        return ans