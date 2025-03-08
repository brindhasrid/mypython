class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high  # After the loop, high is the largest integer where high * high <= x
