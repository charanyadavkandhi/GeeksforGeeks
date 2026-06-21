class Solution:
    def chooseSwap(self, s):
        present = set(s)
        arr = list(s)

        for ch in arr:
            present.discard(ch)

            if not present:
                break

            smallest = min(present)

            if smallest < ch:
                c1, c2 = ch, smallest
                for i in range(len(arr)):
                    if arr[i] == c1:
                        arr[i] = c2
                    elif arr[i] == c2:
                        arr[i] = c1
                return ''.join(arr)

        return s