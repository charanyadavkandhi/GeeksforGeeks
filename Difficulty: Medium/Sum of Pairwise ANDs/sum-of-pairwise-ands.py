class Solution:
    def pairAndSum(self, arr):
        ans = 0
        for bit in range(31):
            count = 0
            for x in arr:
                if x & (1 << bit):
                    count += 1
            ans += count * (count - 1) // 2 * (1 << bit)
        return ans