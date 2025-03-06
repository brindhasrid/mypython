class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: if nums is empty, return 0
        if not nums:
            return 0
        
        # Pointer `i` will keep track of the index for the next unique element
        i = 1
        
        # Traverse the array from the second element (index 1)
        for j in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[j] != nums[j - 1]:
                # Place the unique element at the index `i` and increment `i`
                nums[i] = nums[j]
                i += 1
        
        # `i` will now hold the number of unique elements
        return i
