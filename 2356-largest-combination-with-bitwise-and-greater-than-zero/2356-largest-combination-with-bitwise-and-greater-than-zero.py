class Solution:  
    def largestCombination(self, candidates: List[int]) -> int:  
        bit_counts = [0] * 32  

        for candidate in candidates:  
            for i in range(32):  
                if (candidate >> i) & 1:  
                    bit_counts[i] = max(bit_counts[i], bit_counts[i] + 1)  
        
        return max(bit_counts)