class Solution {  
    public String longestDiverseString(int a, int b, int c) {  
        StringBuilder result = new StringBuilder();  
        int[] counts = {a, b, c};  
        char[] letters = {'a', 'b', 'c'};  

        while (result.length() < a + b + c) {  
            int idx = -1;  
            for (int i = 0; i < 3; i++) {  
                if (counts[i] > 0 && (result.length() < 2 || !(result.charAt(result.length() - 1) == letters[i] && result.charAt(result.length() - 2) == letters[i]))) {  
                    if (idx == -1 || counts[i] > counts[idx]) {  
                        idx = i;  
                    }  
                }  
            }  
            if (idx == -1) {  
                break;  
            }  
            result.append(letters[idx]);  
            counts[idx]--;  
        }  

        return result.toString();  
    }  
}