class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))   
        rank_map = {value: rank + 1 for rank, value in enumerate(sorted_unique)}
    
        return [rank_map[element] for element in arr]