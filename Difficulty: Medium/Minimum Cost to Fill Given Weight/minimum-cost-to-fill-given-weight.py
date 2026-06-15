class Solution:
    def minimumCost(self, cost, w):
        INF = float('inf')

        dp = [INF] * (w + 1)
        dp[0] = 0

        n = len(cost)

        for wt in range(1, n + 1):
            if cost[wt - 1] == -1:
                continue

            for i in range(wt, w + 1):
                dp[i] = min(dp[i],
                            dp[i - wt] + cost[wt - 1])

        return dp[w] if dp[w] != INF else -1