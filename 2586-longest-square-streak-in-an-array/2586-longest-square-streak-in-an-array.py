class Solution(object):  
    def longestSquareStreak(self, nums):  
        nums = sorted(set(nums))  
        num_set = set(nums)  
        max_length = 0  
        
        for number in nums:  
            if number in num_set:  # Check if the number is still in the set  
                streak_length = 1  
                current = number  
                
                while True:  
                    current = current * current  
                    if current in num_set:  
                        streak_length += 1  
                    else:  
                        break  
                
                if streak_length >= 2:  
                    max_length = max(max_length, streak_length)  
        
        return max_length if max_length >= 2 else -1  
        """
        :type nums: List[int]
        :rtype: int
        """
        