class Solution:
    def shortestDist(self, mat):
        n = len(mat)
        ans = [[0] * n for _ in range(n)]
        bad = [[False] * n for _ in range(n)]

        def dfs(i, j):
            if i >= n or j >= n or mat[i][j] == 0:
                return False

            if i == n - 1 and j == n - 1:
                ans[i][j] = 1
                return True

            if bad[i][j]:
                return False

            ans[i][j] = 1

            for jump in range(1, mat[i][j] + 1):

                # right first
                if dfs(i, j + jump):
                    return True

                # down next
                if dfs(i + jump, j):
                    return True

            ans[i][j] = 0
            bad[i][j] = True
            return False

        if dfs(0, 0):
            return ans

        return [[-1]]