class Solution:
    def maxDiffSum(self, arr):
        # code here
        keep = 0
        replace = 0

        for i in range(1, len(arr)):
            new_keep = max(
                keep + abs(arr[i] - arr[i - 1]),
                replace + abs(arr[i] - 1)
            )

            new_replace = max(
                keep + abs(1 - arr[i - 1]),
                replace
            )

            keep = new_keep
            replace = new_replace

        return max(keep, replace)