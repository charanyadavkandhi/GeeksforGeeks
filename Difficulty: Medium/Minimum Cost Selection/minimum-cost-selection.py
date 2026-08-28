class Solution:

    def minCost(self, mat):
        """code here"""
        # dp[j] = minimum cost up to the previous row
        # when choice j was selected in that row.

        dp = mat[0][:]

        for i in range(1, len(mat)):
            a = mat[i]

            new_dp = [0] * 3

            # Choose choice 0 -> previous must be 1 or 2
            new_dp[0] = a[0] + min(dp[1], dp[2])

            # Choose choice 1 -> previous must be 0 or 2
            new_dp[1] = a[1] + min(dp[0], dp[2])

            # Choose choice 2 -> previous must be 0 or 1
            new_dp[2] = a[2] + min(dp[0], dp[1])

            dp = new_dp

        return min(dp)
