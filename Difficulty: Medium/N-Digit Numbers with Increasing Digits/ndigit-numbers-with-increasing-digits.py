class Solution:
    def increasingNumbers(self, n):
        if n == 1:
            return [i for i in range(10)]
        if n > 9:
            return []

        ans = []

        def dfs(num, last_digit, length):
            if length == n:
                ans.append(num)
                return

            for d in range(last_digit + 1, 10):
                dfs(num * 10 + d, d, length + 1)

        for first in range(1, 10):
            dfs(first, first, 1)

        return ans