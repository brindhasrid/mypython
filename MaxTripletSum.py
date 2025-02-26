 
class Solution:
    def maxTripletSum(self, arr): 
        first = second = third = float('-inf')  # Initialize as very small values
        
        for num in arr:
            if num > first:  # If num is the largest so far
                third = second
                second = first
                first = num
            elif num > second:  # If num is the second largest
                third = second
                second = num
            elif num > third:  # If num is the third largest
                third = num
        
        return first + second + third  # Maximum triplet sum

