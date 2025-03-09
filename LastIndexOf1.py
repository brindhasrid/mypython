#User function Template for python3
class Solution:
    def lastIndex(self, s: str) -> int:
        n = len(s)
        # Traverse from last index to first
        for i in range(n - 1, -1, -1):
            if s[i] == '1':  # Compare with '1' (string)
                return i
        return -1  # If no '1' is found

