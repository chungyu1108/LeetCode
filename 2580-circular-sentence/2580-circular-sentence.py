class Solution(object):  
    def isCircularSentence(self, sentence):  
        words = sentence.split()  
        n = len(words)  

        for i in range(n):  
            last_char = words[i][-1]  
            next_first_char = words[(i + 1) % n][0]  
            if last_char != next_first_char:  
                return False  
        
        return True
        """
        :type sentence: str
        :rtype: bool
        """
        