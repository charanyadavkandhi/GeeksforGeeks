class Solution:
    def countSubsequences(self, s, n):
        # code here
        MOD = 10**9 + 7

        dp = [0] * n

        for ch in s:
            digit = int(ch)

            new_dp = dp[:]

            # Start a new subsequence with this digit
            new_dp[digit % n] += 1

            # Add current digit to existing subsequences
            for r in range(n):
                if dp[r]:
                    new_r = (r * 10 + digit) % n
                    new_dp[new_r] = (new_dp[new_r] + dp[r]) % MOD

            dp = new_dp

        return dp[0] % MOD