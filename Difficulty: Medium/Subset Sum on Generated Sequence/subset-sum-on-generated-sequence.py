class Solution:
    def isPossible(self, arr, s, x):
        # dp is a bitset:
        # bit i = 1 means sum i can be formed
        dp = 1
    
        # First number written on paper is s
        if s <= x:
            dp |= dp << s
    
        total = s
    
        for val in arr:
            # Next number written on paper
            current = total + val
    
            # Since all numbers are positive, once current > x,
            # all future numbers will also be > x.
            if current > x:
                break
    
            # Add current number to subset-sum possibilities
            dp |= dp << current
    
            # Keep only sums <= x
            dp &= (1 << (x + 1)) - 1
    
            # Update sum of all numbers currently on paper
            total += current
    
        return ((dp >> x) & 1) == 1
