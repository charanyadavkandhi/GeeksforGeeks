class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])

        height = [0] * m
        ans = 0

        for i in range(n):
            # Calculate consecutive 1s for each column
            for j in range(m):
                if mat[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0

            # IMPORTANT: sort a copy, don't modify height
            arr = sorted(height, reverse=True)

            # Since columns can be swapped
            for j in range(m):
                ans = max(ans, arr[j] * (j + 1))

        return ans
        
        