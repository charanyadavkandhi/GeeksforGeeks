class Solution:
    def maxSumWithK(self, arr, k):
        n = len(arr)

        # Kadane: max subarray sum ending at each index
        maxEnd = [0] * n
        maxEnd[0] = arr[0]

        for i in range(1, n):
            maxEnd[i] = max(arr[i], maxEnd[i - 1] + arr[i])

        # Initial window of size k
        windowSum = sum(arr[:k])
        ans = windowSum

        # Slide the window
        for i in range(k, n):
            windowSum += arr[i] - arr[i - k]
            ans = max(ans, windowSum)
            ans = max(ans, windowSum + maxEnd[i - k])

        return ans