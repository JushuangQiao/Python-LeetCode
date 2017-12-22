class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
