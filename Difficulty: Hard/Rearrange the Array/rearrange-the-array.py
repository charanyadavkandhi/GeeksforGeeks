class Solution:
    def minOperations(self, b):
        MOD = 10**9 + 7
        n = len(b)

        # Find cycle lengths
        visited = [False] * n
        cycle_lengths = []

        for i in range(n):
            if not visited[i]:
                cnt = 0
                cur = i
                while not visited[cur]:
                    visited[cur] = True
                    cur = b[cur] - 1   # convert to 0-based index
                    cnt += 1
                cycle_lengths.append(cnt)

        # Sieve for smallest prime factor
        spf = list(range(n + 1))
        i = 2
        while i * i <= n:
            if spf[i] == i:
                j = i * i
                while j <= n:
                    if spf[j] == j:
                        spf[j] = i
                    j += i
            i += 1

        # Store maximum exponent of each prime
        max_exp = {}

        for x in cycle_lengths:
            temp = x
            while temp > 1:
                p = spf[temp]
                e = 0
                while temp % p == 0:
                    temp //= p
                    e += 1
                if p not in max_exp or max_exp[p] < e:
                    max_exp[p] = e

        # Compute LCM modulo MOD
        ans = 1
        for p, e in max_exp.items():
            ans = (ans * pow(p, e, MOD)) % MOD

        return ans