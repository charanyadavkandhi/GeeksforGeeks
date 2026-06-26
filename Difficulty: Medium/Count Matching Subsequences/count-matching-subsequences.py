class Solution:
    def countWays(self, s1, s2):
        MOD = 10**9 + 7
        m, n = len(s1), len(s2)

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(m):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[j + 1] = (dp[j + 1] + dp[j]) % MOD

        return dp[n]