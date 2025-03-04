#User function template for Python
class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, k):
        n = len(arr)
        for i in range(0, n, k):  # Iterate with step size k
            arr[i:i+k] = arr[i:i+k][::-1]  # Reverse sub-array in place

