from math import gcd

class Solution:
    def sameMod(self, arr):
        # If all elements are equal, infinitely many k are possible
        if len(set(arr)) == 1:
            return -1

        # Find GCD of differences
        g = 0

        for i in range(1, len(arr)):
            g = gcd(g, abs(arr[i] - arr[0]))

        # Count divisors of g
        ans = 0

        for k in range(1, int(g ** 0.5) + 1):
            if g % k == 0:
                ans += 1

                if k != g // k:
                    ans += 1

        return ans