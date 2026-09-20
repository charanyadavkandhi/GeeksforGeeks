class Solution:
    def largestSubsquare(self, mat):
        n = len(mat)
        if n == 0:
            return 0

        right = [[0] * (n + 1) for _ in range(n + 1)]
        down = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            row = mat[i]
            r_cur, r_next = right[i], right[i + 1]
            d_cur, d_next = down[i], down[i + 1]
            for j in range(n - 1, -1, -1):
                if row[j] == 'X':
                    r_cur[j] = r_cur[j + 1] + 1
                    d_cur[j] = d_next[j] + 1

        best = 0
        for i in range(n):
            r_i, d_i = right[i], down[i]
            for j in range(n):
                limit = r_i[j]
                if limit > best:
                    d = d_i[j]
                    if d < limit:
                        limit = d
                    for k in range(limit, best, -1):
                        if right[i + k - 1][j] >= k and down[i][j + k - 1] >= k:
                            best = k
                            break
        return best