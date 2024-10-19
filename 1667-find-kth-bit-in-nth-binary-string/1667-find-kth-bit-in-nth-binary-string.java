class Solution {  
    public char findKthBit(int n, int k) {  
        if (n == 1) {  
            return '0';  
        }  
        
        int len = (1 << n) - 1;  
        
        if (k == (len / 2) + 1) {  
            return '1';  
        } else if (k <= len / 2) {  
            return findKthBit(n - 1, k);  
        } else {  
            int newK = len - k;  
            char bit = findKthBit(n - 1, newK + 1);  
            return bit == '0' ? '1' : '0';  
        }  
    }  
}