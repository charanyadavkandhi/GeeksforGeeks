class Solution:
    def kthSmallest(self, arr, k):
        def partition(left, right):
            pivot = arr[right]
            i = left

            for j in range(left, right):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[i], arr[right] = arr[right], arr[i]
            return i

        def quickSelect(left, right):
            if left <= right:
                p = partition(left, right)

                if p == k - 1:
                    return arr[p]
                elif p > k - 1:
                    return quickSelect(left, p - 1)
                else:
                    return quickSelect(p + 1, right)

        return quickSelect(0, len(arr) - 1)