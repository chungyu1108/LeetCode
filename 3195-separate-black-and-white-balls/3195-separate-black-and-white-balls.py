class Solution:  
    def minimumSteps(self, s: str) -> int:  
        swaps = 0  
        count_ones = 0  
        
        for char in s:  
            if char == '1':  
                count_ones += 1  
            else:  
                swaps += count_ones  
        
        return swaps  