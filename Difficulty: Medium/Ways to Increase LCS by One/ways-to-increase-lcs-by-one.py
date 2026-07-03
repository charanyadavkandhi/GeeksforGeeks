class Solution:
    def waysToIncreaseLCSBy1(self, s1, s2):
        n, m = len(s1), len(s2)
        pre = [[0]*(m+1) for _ in range(n+1)]
        suf = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                pre[i+1][j+1] = pre[i][j]+1 if s1[i]==s2[j] else max(pre[i][j+1], pre[i+1][j])

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                suf[i][j] = suf[i+1][j+1]+1 if s1[i]==s2[j] else max(suf[i+1][j], suf[i][j+1])

        l = pre[n][m]
        ans = 0

        for i in range(n+1):
            vis = set()
            for j in range(m):
                if s2[j] not in vis and pre[i][j]+1+suf[i][j+1] == l+1:
                    ans += 1
                    vis.add(s2[j])

        return ans