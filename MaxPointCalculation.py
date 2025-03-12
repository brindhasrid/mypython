#User function Template for python3

class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        result=0
        for num in arr:
            result^=num
            
        return result

