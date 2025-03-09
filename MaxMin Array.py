
class Solution:
    def get_min_max(self, arr):
        i=0
        min=arr[i]
        max=arr[i]
        for i in range (1,len(arr)):
            if arr[i]>max:
                max=arr[i]
            if arr[i]<min:
                min=arr[i]
        return min, max
