class Solution:
    def largestArea(self, n, m, arr):
        rows = [0, n + 1]
        cols = [0, m + 1]

        for r, c in arr:
            rows.append(r)
            cols.append(c)

        rows.sort()
        cols.sort()

        maxr = 0
        for i in range(1, len(rows)):
            maxr = max(maxr, rows[i] - rows[i - 1] - 1)

        maxc = 0
        for i in range(1, len(cols)):
            maxc = max(maxc, cols[i] - cols[i - 1] - 1)

        return maxr * maxc