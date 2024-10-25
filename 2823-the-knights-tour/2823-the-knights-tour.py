class Solution(object):  
    def tourOfKnight(self, m, n, r, c):  
        board = [[-1 for _ in range(n)] for _ in range(m)]  
        moves = [  
            (2, 1), (1, 2), (-1, 2), (-2, 1),  
            (-2, -1), (-1, -2), (1, -2), (2, -1)  
        ]  
        
        def is_valid(x, y):  
            return 0 <= x < m and 0 <= y < n and board[x][y] == -1  

        def backtrack(x, y, move_count):  
            if move_count == m * n:  
                return True  
            
            for dx, dy in moves:  
                new_x, new_y = x + dx, y + dy  
                if is_valid(new_x, new_y):  
                    board[new_x][new_y] = move_count  
                    if backtrack(new_x, new_y, move_count + 1):  
                        return True  
                    board[new_x][new_y] = -1  
            
            return False  

        board[r][c] = 0  
        if backtrack(r, c, 1):  
            return board  
        else:  
            return []  
        """
        :type m: int
        :type n: int
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        