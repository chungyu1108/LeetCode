class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        i = 2  # Start from the third element (since the first two are always allowed)
        
        for j in range(2, len(nums)):
            # If the current number is different from the number at i-2 position, place it at i
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        
        return i