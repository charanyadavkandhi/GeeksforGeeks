class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        """ code here """
        n = len(arr)

        if m >= n:
            return sum(arr)

        # Make the circle into a linear array
        b = arr + arr

        # First window of size m
        current = sum(b[:m])
        ans = current

        # Check all n possible starting positions
        for i in range(1, n):
            current -= b[i - 1]
            current += b[i + m - 1]

            ans = max(ans, current)

        return ans
