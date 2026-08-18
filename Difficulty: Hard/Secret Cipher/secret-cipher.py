class Solution:
    def compress(self, s):
        n = len(s)

        # LPS (Longest Prefix Suffix) array
        lps = [0] * n

        for i in range(1, n):
            j = lps[i - 1]

            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]

            if s[i] == s[j]:
                j += 1

            lps[i] = j

        ans = []
        i = n - 1

        while i >= 0:
            length = i + 1

            # Only even-length prefixes can be doubled
            if length % 2 == 0:
                common = lps[i]
                period = length - common

                # Check whether the whole prefix is made
                # of two identical parts
                if common * 2 >= length and length % (2 * period) == 0:
                    ans.append('*')

                    # Move to the end of the first half
                    i = i // 2 + 1
                else:
                    ans.append(s[i])
            else:
                ans.append(s[i])

            i -= 1

        return ''.join(reversed(ans))