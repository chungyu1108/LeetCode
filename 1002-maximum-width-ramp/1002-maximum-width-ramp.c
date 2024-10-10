int maxWidthRamp(int* nums, int numsSize) {
    int stack[numsSize];
    int stackSize = 0;
    
    for (int i = 0; i < numsSize; i++) {
        if (stackSize == 0 || nums[stack[stackSize - 1]] > nums[i]) {
            stack[stackSize++] = i;
        }
    }
    
    int maxRampWidth = 0;
    for (int j = numsSize - 1; j >= 0; j--) {
        while (stackSize > 0 && nums[j] >= nums[stack[stackSize - 1]]) {
            int i = stack[--stackSize]; 
            if (j - i > maxRampWidth) {
                maxRampWidth = j - i; 
            }
        }
    }
    
    return maxRampWidth;
}