class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        # code here
        dist = [0] * V

        # Relax all edges V-1 times
        for _ in range(V - 1):
            updated = False

            for u, v, w in edges:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    updated = True

            if not updated:
                break

        # One more relaxation to detect negative cycle
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                return True

        return False