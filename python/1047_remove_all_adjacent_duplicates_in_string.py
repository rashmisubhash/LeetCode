# 1047. Remove All Adjacent Duplicates In String

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Use a stack to store the string
        # Pop the top if the char matches
        # Useful using a stack as even when the elements are removed, one can still get the top
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
        
        

        