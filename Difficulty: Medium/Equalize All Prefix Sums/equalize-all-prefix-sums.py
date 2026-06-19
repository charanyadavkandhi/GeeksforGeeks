class Solution:
    def optimalArray(self, arr):
        n = len(arr)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        ans = []

        for i in range(n):
            m = i // 2
            median = arr[m]

            left_cost = median * (m + 1) - prefix[m + 1]
            right_cost = (prefix[i + 1] - prefix[m + 1]) - median * (i - m)

            ans.append(left_cost + right_cost)

        return ans