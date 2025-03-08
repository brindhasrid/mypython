class Solution:
    def countOfElements(self, x, arr):
        count = 0  # Initialize the counter to zero
        for num in arr:  # Iterate through each element in the array
            if num <= x:  # If the current element is less than or equal to x
                count += 1  # Increment the counter
        return count  # Return the final count
