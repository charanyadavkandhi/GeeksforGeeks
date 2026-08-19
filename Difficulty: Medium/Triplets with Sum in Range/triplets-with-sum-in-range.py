class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        # code here
        arr.sort()

        def count_at_most(x):
            n = len(arr)
            count = 0

            for i in range(n - 2):
                left = i + 1
                right = n - 1

                while left < right:
                    total = arr[i] + arr[left] + arr[right]

                    if total <= x:
                        count += right - left
                        left += 1
                    else:
                        right -= 1

            return count

        return count_at_most(r) - count_at_most(l - 1)