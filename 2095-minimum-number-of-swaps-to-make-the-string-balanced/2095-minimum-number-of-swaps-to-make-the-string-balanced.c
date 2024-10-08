int minSwaps(char* s) {
    int balance = 0;    
    int swaps_needed = 0; 

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '[') {
            balance++;  
        } else { 
            balance--; 
        }

        if (balance < 0) {
            swaps_needed++;
            balance += 2; 
        }
    }

    return swaps_needed; 
}