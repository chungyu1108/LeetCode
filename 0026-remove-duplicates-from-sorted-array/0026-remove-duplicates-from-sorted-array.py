class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r -1]:
                nums[s] = nums[r]
                s += 1
        return s