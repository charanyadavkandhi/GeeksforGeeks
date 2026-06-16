class Solution:
    def constructList(self, queries):
        curXor = 0
        arr = [0]

        for typ, x in queries:
            if typ == 0:
                arr.append(x ^ curXor)
            else:
                curXor ^= x

        ans = [num ^ curXor for num in arr]
        ans.sort()

        return ans