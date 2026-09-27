class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                # Extract characters until the matching '('
                curr = []
                while stack and stack[-1] != '(':
                    curr.append(stack.pop())
                # Remove the '(' from the stack
                if stack and stack[-1] == '(':
                    stack.pop()
                # Push the reversed characters back onto the stack
                stack.extend(curr)
            else:
                stack.append(char)
        
        return "".join(stack)