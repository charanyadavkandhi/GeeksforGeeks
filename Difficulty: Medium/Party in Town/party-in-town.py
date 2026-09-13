class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        n = len(adj)

        def bfs(start):
            dist = [-1] * n
            dist[start] = 0

            queue = [start]
            front = 0
            farthest = start

            while front < len(queue):
                node = queue[front]
                front += 1

                if dist[node] > dist[farthest]:
                    farthest = node

                for nei in adj[node]:
                    nei -= 1  # houses are numbered 1 to n

                    if dist[nei] == -1:
                        dist[nei] = dist[node] + 1
                        queue.append(nei)

            return farthest, dist[farthest]

        # Find one endpoint of the diameter
        endpoint, _ = bfs(0)

        # Find the diameter length
        _, diameter = bfs(endpoint)

        return (diameter + 1) // 2