class Solution(object):  
    def removeSubfolders(self, folder):  
        folder.sort()  
        result = []  
        prev = None  
        
        for f in folder:  
            if prev is None or not f.startswith(prev + '/'):  
                result.append(f)  
                prev = f  

        return result
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        