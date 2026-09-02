class Solution:
    def solve(self, n, s):
        # code here
        using = set()
        rejected = set()
        ans = 0

        for ch in s:
            if ch in using:
                # Assigned customer leaves
                using.remove(ch)

            elif ch in rejected:
                # Rejected customer's second occurrence
                rejected.remove(ch)

            else:
                # Customer arrives
                if len(using) < n:
                    using.add(ch)
                else:
                    rejected.add(ch)
                    ans += 1

        return ans