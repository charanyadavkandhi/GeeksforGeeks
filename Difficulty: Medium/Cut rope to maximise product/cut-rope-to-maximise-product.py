class Solution:
    def maxProduct(self, n):
        # Base cases
        if n == 2:
            return 1
        if n == 3:
            return 2

        product = 1

        # Cut the rope into pieces of length 3
        while n > 4:
            product *= 3
            n -= 3

        # Multiply the remaining part
        product *= n

        return product