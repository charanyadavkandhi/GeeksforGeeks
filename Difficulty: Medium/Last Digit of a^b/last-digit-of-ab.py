class Solution:
    def getLastDigit(self, a, b):
        if b == "0":
            return 1

        x = int(a[-1])
        e = 0
        for ch in b:
            e = (e * 10 + int(ch)) % 4
        if e == 0:
            e = 4

        return pow(x, e, 10)