class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for char in s:
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()  # Remove the pair "AB" or "CD"
            else:
                stack.append(char)  # Keep the current character
                
        return len(stack)