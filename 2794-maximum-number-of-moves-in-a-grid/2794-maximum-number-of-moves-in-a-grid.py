class Solution(object):  
    def maxMoves(self, grid):  
        m, n = len(grid), len(grid[0])  
        memo = [[-1] * n for _ in range(m)]  # Memoization table  

        def dfs(row, col):  
            if memo[row][col] != -1:  
                return memo[row][col]  # Return cached result  

            max_moves = 0  
            # Possible moves: right-up, right, right-down  
            for new_row in (row - 1, row, row + 1):  
                if 0 <= new_row < m and col + 1 < n and grid[new_row][col + 1] > grid[row][col]:  
                    max_moves = max(max_moves, 1 + dfs(new_row, col + 1))  

            memo[row][col] = max_moves  # Cache the result  
            return max_moves  

        max_result = 0  
        # Start from any cell in the first column  
        for i in range(m):  
            max_result = max(max_result, dfs(i, 0))  

        return max_result
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        