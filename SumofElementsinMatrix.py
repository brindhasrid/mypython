#User function Template for python3

class Solution:
    def sumOfMatrix(self,N,M,Grid):
        #code here
        total_sum = 0
        for i in range(N):
            for j in range(M):
                total_sum += Grid[i][j]
        return total_sum

