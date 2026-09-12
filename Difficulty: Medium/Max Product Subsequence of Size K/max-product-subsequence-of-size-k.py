class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:
        # dp[j] = [minimum product, maximum product]
        # using exactly j elements
        dp = [[float('inf'), float('-inf')] for _ in range(k + 1)]

        dp[0] = [1, 1]

        for x in arr:
            # Go backwards so each element is used at most once
            for j in range(min(k, len(arr)), 0, -1):
                if dp[j - 1][1] == float('-inf'):
                    continue

                mn, mx = dp[j - 1]

                candidates = [
                    mn * x,
                    mx * x
                ]

                new_min = min(candidates)
                new_max = max(candidates)

                dp[j][0] = min(dp[j][0], new_min)
                dp[j][1] = max(dp[j][1], new_max)

        return dp[k][1]