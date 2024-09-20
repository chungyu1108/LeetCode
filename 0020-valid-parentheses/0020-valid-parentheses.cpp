class Solution {
public:
    bool isValid(string s) {
        // Stack to keep track of opening brackets
        std::stack<char> stack;

        // Map to match the closing brackets with their corresponding opening ones
        std::unordered_map<char, char> bracket_map = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        // Traverse through the string
        for (char c : s) {
            // If it's a closing bracket
            if (bracket_map.count(c)) {
                // Check if the stack is empty or the top of the stack doesn't match the corresponding opening bracket
                if (stack.empty() || stack.top() != bracket_map[c]) {
                    return false;
                }
                // If it matches, pop the opening bracket from the stack
                stack.pop();
            } else {
                // If it's an opening bracket, push it onto the stack
                stack.push(c);
            }
        }

        // If the stack is empty, all opening brackets have been matched; otherwise, it's invalid
        return stack.empty();
    }
};