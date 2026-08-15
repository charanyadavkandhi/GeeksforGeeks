class Solution:

    def countWithout(self, n: int, d: int) -> int:
        # code here
        s = str(n)

        from functools import lru_cache

        @lru_cache(None)
        def dp(pos, tight, started):
            if pos == len(s):
                return 1 if started else 0

            limit = int(s[pos]) if tight else 9
            ans = 0

            for digit in range(limit + 1):
                new_tight = tight and (digit == limit)

                # Leading zero
                if not started and digit == 0:
                    ans += dp(pos + 1, new_tight, False)
                else:
                    # Do not allow digit d
                    if digit == d:
                        continue

                    ans += dp(pos + 1, new_tight, True)

            return ans

        return dp(0, True, False)