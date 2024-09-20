class Solution:
    def shortestPalindrome(self, s: str) -> str:
           
        rev_s = s[::-1]
    
        new_s = s + "#" + rev_s
    
    # Compute the KMP table (prefix function)
        n = len(new_s)
        lps = [0] * n  # Longest Prefix Suffix table
    
    # Build the LPS array
        for i in range(1, n):
            j = lps[i - 1]
        
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]
        
            if new_s[i] == new_s[j]:
                j += 1
        
            lps[i] = j
    

        longest_palindrome_length = lps[-1]
    

        suffix_to_add = rev_s[:len(s) - longest_palindrome_length]
    
        return suffix_to_add + s