class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # 32-bit integer range
        rev = 0
        sign = -1 if x < 0 else 1  # Store sign
        
        x = abs(x)  # Work with positive number
        while x != 0:
            digit = x % 10  # Extract last digit
            x //= 10  # Remove last digit
            
            # Check for overflow BEFORE multiplying by 10
            if rev > (INT_MAX - digit) // 10:
                return 0  # Return 0 if it overflows
            
            rev = rev * 10 + digit  # Construct reversed number
        
        return sign * rev  # Restore original sign

# Example usage:
solution = Solution()
print(solution.reverse(123))   # Output: 321
print(solution.reverse(-123))  # Output: -321
print(solution.reverse(120))   # Output: 21
print(solution.reverse(1534236469))  # Output: 0 (Overflow case)
