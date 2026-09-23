class Solution:
    def formPyramid(self, arr):
        n = len(arr)

        left = [0] * n
        right = [0] * n

        # Maximum possible increasing sequence ending at i
        left[0] = min(arr[0], 1)

        for i in range(1, n):
            left[i] = min(arr[i], left[i - 1] + 1)

        # Maximum possible decreasing sequence starting at i
        right[n - 1] = min(arr[n - 1], 1)

        for i in range(n - 2, -1, -1):
            right[i] = min(arr[i], right[i + 1] + 1)

        # Find the maximum pyramid we can keep
        max_kept = 0

        for i in range(n):
            height = min(left[i], right[i])
            max_kept = max(max_kept, height * height)

        return sum(arr) - max_kept