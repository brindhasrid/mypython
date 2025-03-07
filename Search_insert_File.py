class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        # Perform binary search
        while left <= right:
            mid = (left + right) // 2  # Find the middle index
            
            if nums[mid] == target:
                return mid  # Target found, return the index
            elif nums[mid] < target:
                left = mid + 1  # Target must be in the right half
            else:
                right = mid - 1  # Target must be in the left half
        
        # If the target was not found, `left` is the insertion index
        return left
