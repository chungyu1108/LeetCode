class Solution:  
    def smallestRange(self, nums: List[List[int]]) -> List[int]:  
        min_heap = []  
        max_num = float('-inf')  
        range_start, range_end = -1, -1  
        min_range = float('inf')  
        
        for i in range(len(nums)):  
            heapq.heappush(min_heap, (nums[i][0], i, 0))  
            max_num = max(max_num, nums[i][0])  
        
        while True:  
            min_num, list_index, element_index = heapq.heappop(min_heap)  

            if max_num - min_num < min_range:  
                min_range = max_num - min_num  
                range_start, range_end = min_num, max_num  
            
            if element_index + 1 == len(nums[list_index]):  
                break  
            
            next_num = nums[list_index][element_index + 1]  
            heapq.heappush(min_heap, (next_num, list_index, element_index + 1))  
            max_num = max(max_num, next_num)  
        
        return [range_start, range_end]