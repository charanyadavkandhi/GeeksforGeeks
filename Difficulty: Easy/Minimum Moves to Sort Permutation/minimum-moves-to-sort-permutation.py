class Solution:
    def minMoves(self, arr):
        n = len(arr)

# pos[x] = position of value x in the array
        pos = [0] * (n + 1)

        for i in range(n):
            pos[arr[i]] = i

# Find the longest consecutive sequence
# whose positions are also increasing.
        longest = 1
        current = 1

        for x in range(2, n + 1):
            if pos[x] > pos[x - 1]:
                current += 1
            else:
                current = 1

            longest = max(longest, current)

        return n - longest