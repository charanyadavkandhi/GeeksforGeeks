class Solution:
    def searchWord(self, mat, word):
        n = len(mat)
        m = len(mat[0])

        # 8 possible directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        ans = []

        for i in range(n):
            for j in range(m):

                # First character must match
                if mat[i][j] != word[0]:
                    continue

                # Try all 8 directions
                for dr, dc in directions:
                    k = 1

                    while k < len(word):
                        ni = i + dr * k
                        nj = j + dc * k

                        # Outside grid
                        if ni < 0 or ni >= n or nj < 0 or nj >= m:
                            break

                        # Character doesn't match
                        if mat[ni][nj] != word[k]:
                            break

                        k += 1

                    # Entire word matched
                    if k == len(word):
                        ans.append([i, j])
                        break

        return ans