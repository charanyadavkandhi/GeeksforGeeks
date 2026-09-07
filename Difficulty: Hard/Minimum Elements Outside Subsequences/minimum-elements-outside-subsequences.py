class Solution:
    def minCount(self, arr):
        n = len(arr)

        # dp[inc][dec] = maximum selected elements
        # inc: last value of increasing subsequence
        # dec: last value of decreasing subsequence
        #
        # inc starts at 0 because arr[i] >= 1
        # dec starts at 101 because arr[i] <= 100
        dp = [[-1] * 102 for _ in range(101)]

        dp[0][101] = 0

        for x in arr:
            new_dp = [row[:] for row in dp]

            for inc in range(101):
                for dec in range(102):
                    if dp[inc][dec] == -1:
                        continue

                    current = dp[inc][dec]

                    # Put x in increasing subsequence
                    if x > inc:
                        new_dp[x][dec] = max(
                            new_dp[x][dec],
                            current + 1
                        )

                    # Put x in decreasing subsequence
                    if x < dec:
                        new_dp[inc][x] = max(
                            new_dp[inc][x],
                            current + 1
                        )

            dp = new_dp

        # Maximum number of elements included
        maximum_selected = 0

        for inc in range(101):
            for dec in range(102):
                maximum_selected = max(
                    maximum_selected,
                    dp[inc][dec]
                )

        return n - maximum_selected