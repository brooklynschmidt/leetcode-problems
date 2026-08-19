class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Use a stack to view last appended paren
        # Since they need to be valid parens, the most recent open should follow the most recently seen closed
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
                continue
            elif char == ')' and len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop()
                    continue
                else:
                    return False
            elif char == ']' and len(stack) > 0:
                if stack[-1] == '[':
                    stack.pop()
                    continue
                else:
                    return False
            elif char == '}' and len(stack) > 0:
                if stack[-1] == '{':
                    stack.pop()
                    continue
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0
