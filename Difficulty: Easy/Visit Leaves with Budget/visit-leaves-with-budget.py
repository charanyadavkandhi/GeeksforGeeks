class Solution:
    def getCount(self, root, k):
        if not root:
            return 0

        leaf_levels = []

        # DFS: (node, level)
        stack = [(root, 1)]

        while stack:
            node, level = stack.pop()

            # Leaf node
            if not node.left and not node.right:
                leaf_levels.append(level)
                continue

            if node.left:
                stack.append((node.left, level + 1))

            if node.right:
                stack.append((node.right, level + 1))

        # Cheapest leaves first
        leaf_levels.sort()

        count = 0

        for cost in leaf_levels:
            if cost > k:
                break

            k -= cost
            count += 1

        return count