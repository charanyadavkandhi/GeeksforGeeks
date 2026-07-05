class Solution:
    def checkStatus(self, a, b, flag):
        if flag:
            return a < 0 and b < 0
        else:
            return (a >= 0) != (b >= 0)