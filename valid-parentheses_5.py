"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Stack to keep track of opening brackets
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                #Check the top of the stack (last opening bracket) or use a dummy value if the stack is empty
                top_element = stack.pop() if stack else '#'
                
                # If the bracket doesn't match, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all opening brackets were matched properly, so return True
        return not stack
