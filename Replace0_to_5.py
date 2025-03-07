class Solution:
    def convertFive(self, n):
        # Convert integer to string
        n_str = str(n)
        
        # Replace all zeros with '5'
        n_str = n_str.replace('0', '5')
        
        # Convert the modified string back to integer and return
        return int(n_str)
