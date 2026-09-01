class Solution:
    def palindromicStrings(self, n, k):
        # code here
        MOD = 10**9 + 7

        ans = 0
        ways = 1  # number of ways to choose first half

        for h in range(n // 2 + 1):

            if h > 0:
                ways = ways * (k - h + 1) % MOD

            # Even length: 2*h
            # Exclude h = 0 because empty string is not allowed
            if h > 0 and 2 * h <= n:
                ans = (ans + ways) % MOD

            # Odd length: 2*h + 1
            if 2 * h + 1 <= n:
                ans = (ans + ways * (k - h)) % MOD

        return ans