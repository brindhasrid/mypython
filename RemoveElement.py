class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0  # This will track the index where the next non-val element will go
        
        for read_index in range(len(nums)):  # Iterate over all elements in nums
            if nums[read_index] != val:  # If the current element is not equal to val
                nums[write_index] = nums[read_index]  # Place it at the write_index
                write_index += 1  # Increment write_index to the next position
        
        return write_index  # The number of elements that are not equal to val
