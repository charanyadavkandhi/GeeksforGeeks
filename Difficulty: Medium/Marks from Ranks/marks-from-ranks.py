class Solution:

    def getMarks(self, l, r, rank):
        n = len(l)

        # Prefix count of valid marks
        prefix = [0] * n

        for i in range(n):
            prefix[i] = r[i] - l[i] + 1

            if i > 0:
                prefix[i] += prefix[i - 1]

        ans = []

        for k in rank:
            # Binary search for the interval containing rank k
            low, high = 0, n - 1

            while low < high:
                mid = (low + high) // 2

                if prefix[mid] >= k:
                    high = mid
                else:
                    low = mid + 1

            i = low

            # Number of marks before this interval
            before = 0 if i == 0 else prefix[i - 1]

            # Find actual mark
            mark = l[i] + (k - before - 1)

            ans.append(mark)

        return ans
