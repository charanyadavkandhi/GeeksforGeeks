class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        n = len(s1)
        m = len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Delete all characters from s1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + costS1

        # Delete all characters from s2
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + costS2

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    delete_s1 = dp[i - 1][j] + costS1
                    delete_s2 = dp[i][j - 1] + costS2

                    dp[i][j] = min(delete_s1, delete_s2)

        return dp[n][m]