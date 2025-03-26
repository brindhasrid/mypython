class Solution:
    def singleNumber(self, arr):
        # Step 1: XOR all elements to get XOR of the two unique numbers
        xor_all = 0
        for num in arr:
            xor_all ^= num

        # Step 2: Find a set bit (rightmost) in xor_all to differentiate the two numbers
        set_bit = xor_all & -xor_all

        # Step 3: Divide numbers into two groups and XOR separately
        num1 = num2 = 0
        for num in arr:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num

        # Step 4: Return the result in increasing order
        return sorted([num1, num2])

# Example usage
solution = Solution()
ans = solution.singleNumber([1, 2, 3, 2, 1, 4])
if ans:
    print(" ".join(map(str, ans)))  # Output: 3 4

ans = solution.singleNumber([2, 1, 3, 2])
if ans:
    print(" ".join(map(str, ans)))  # Output: 1 3

ans = solution.singleNumber([2, 1, 3, 3])
if ans:
    print(" ".join(map(str, ans)))  # Output: 1 2
