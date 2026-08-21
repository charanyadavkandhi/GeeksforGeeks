class Solution:
    def transform(self, s1, s2): 
        #code here
        if len(s1) != len(s2):
            return -1

        # Both strings must contain the same characters
        if sorted(s1) != sorted(s2):
            return -1

        i = len(s1) - 1
        j = len(s2) - 1

        # Find the longest suffix of s1 that is already
        # in the correct relative order in s2
        while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                j -= 1
            i -= 1

        # Characters not matched need to be moved to front
        return j + 1