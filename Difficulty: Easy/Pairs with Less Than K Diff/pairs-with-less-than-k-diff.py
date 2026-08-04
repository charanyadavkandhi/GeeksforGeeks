class Solution:
    def countPairs(self, arr, k):
        arr.sort()
        n = len(arr)
        i = 0
        ans = 0

        for j in range(n):
            while arr[j] - arr[i] >= k:
                i += 1
            ans += j - i

        return ans