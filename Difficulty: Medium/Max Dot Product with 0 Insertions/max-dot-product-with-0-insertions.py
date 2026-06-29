class Solution:
    def maxDotProduct(self, a, b):
        n = len(a)
        m = len(b)

        NEG = -10**18

        dp = [NEG] * (m + 1)
        dp[0] = 0

        for i in range(n):
            for j in range(min(i + 1, m), 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + a[i] * b[j - 1])

        return dp[m]