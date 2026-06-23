class Solution:
    def maxPeopleDefeated(self, p):
        low, high = 0, int((6 * p) ** (1/3)) + 5

        while low <= high:
            mid = (low + high) // 2
            total = mid * (mid + 1) * (2 * mid + 1) // 6

            if total <= p:
                low = mid + 1
            else:
                high = mid - 1

        return high