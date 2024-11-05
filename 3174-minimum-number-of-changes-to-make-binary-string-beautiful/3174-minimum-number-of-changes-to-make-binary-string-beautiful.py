class Solution(object):  
    def minChanges(self, s):  
        n = len(s)  
        changes_to_zero = 0  
        changes_to_one = 0  
        
        for i in range(0, n, 2):  
            if s[i] == s[i + 1]:  
                continue  
            else:  
                changes_to_zero += 1  
                changes_to_one += 1  
        
        return min(changes_to_zero, changes_to_one)  

        """
        :type s: str
        :rtype: int
        """
        