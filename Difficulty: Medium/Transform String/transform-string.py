class Solution:
    def transform(self, s1, s2): 
        #code here
        if len(s1) != len(s2):
            return -1

        # Check whether both strings contain the same characters
        freq = [0] * 256

        for ch in s1:
            freq[ord(ch)] += 1

        for ch in s2:
            freq[ord(ch)] -= 1

        for x in freq:
            if x != 0:
                return -1

        i = len(s1) - 1
        j = len(s2) - 1
        ans = 0

        while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                i -= 1
                j -= 1
            else:
                ans += 1
                i -= 1

        return ans