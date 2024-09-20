class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        statusPosition = [False for i in range(len(nums))]
        statusPosition[0] = True

        i = 0
        for maxR in range(1, len(nums)):
            while i < maxR:
                if statusPosition[i] and nums[i] + i >= maxR:
                    statusPosition[maxR] = True
                    break
                i += 1

        return statusPosition[-1]
