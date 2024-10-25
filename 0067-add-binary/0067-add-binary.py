class Solution(object):  
    def addBinary(self, a, b):  
        i, j = len(a) - 1, len(b) - 1  
        carry = 0  
        result = []  
        
        while i >= 0 or j >= 0 or carry:  
            bit_a = int(a[i]) if i >= 0 else 0  
            bit_b = int(b[j]) if j >= 0 else 0  
            total = bit_a + bit_b + carry  
            carry = total // 2  
            result.append(str(total % 2))  
            i -= 1  
            j -= 1  
        
        return ''.join(result[::-1])
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        