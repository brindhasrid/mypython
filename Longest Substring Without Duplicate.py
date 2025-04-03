class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        left = 0  # Left pointer of the sliding window

        for right in range(len(s)):
            if s[right] in char_index:
                # Move left to avoid duplicates, ensuring it never moves backward
                left = max(left, char_index[s[right]] + 1)

            # Store/update the last index of the character
            char_index[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length

# Example usage:
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3
