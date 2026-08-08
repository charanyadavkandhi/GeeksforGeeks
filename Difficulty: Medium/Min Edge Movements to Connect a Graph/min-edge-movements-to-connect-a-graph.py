class Solution:
    def minEdgesReq(self, n, edges):
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False  # redundant edge

            if rank[pa] < rank[pb]:
                pa, pb = pb, pa

            parent[pb] = pa

            if rank[pa] == rank[pb]:
                rank[pa] += 1

            return True

        # Count redundant edges
        extra = 0

        for u, v in edges:
            if not union(u, v):
                extra += 1

        # Count connected components
        components = 0
        for i in range(n):
            if find(i) == i:
                components += 1

        # Need components - 1 edges to connect all components
        required = components - 1

        if extra >= required:
            return required

        return -1