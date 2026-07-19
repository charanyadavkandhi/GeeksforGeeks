class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)

        # upEnd[i] = farthest index reachable from i while staying non-decreasing
        upEnd = [0] * n
        upEnd[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                upEnd[i] = upEnd[i + 1]
            else:
                upEnd[i] = i

        # downEnd[i] = farthest index reachable from i while staying non-increasing
        downEnd = [0] * n
        downEnd[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                downEnd[i] = downEnd[i + 1]
            else:
                downEnd[i] = i

        ans = []
        for l, r in queries:
            peak = upEnd[l]
            ans.append(downEnd[peak] >= r)

        return ans