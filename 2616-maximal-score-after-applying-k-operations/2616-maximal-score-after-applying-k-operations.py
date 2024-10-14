class Solution:  
    def maxKelements(self, nums: List[int], k: int) -> int:  
        max_heap = [-num for num in nums]  
        heapq.heapify(max_heap)  
        score = 0  
        
        for _ in range(k):  
            max_elem = -heapq.heappop(max_heap)  
            score += max_elem  
            new_elem = ceil(max_elem / 3)  
            heapq.heappush(max_heap, -new_elem)  
        
        return score  

