#User function Template for python3

class Solution:
    def multiply(self, arr):
        # Code here
        n=len(arr)
        mid=n//2
        right_sum=sum(arr[:mid])
        left_sum=sum(arr[mid:])
        return right_sum*left_sum
