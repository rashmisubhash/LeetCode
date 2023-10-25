# 1021. Remove Outermost Parentheses

class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        open_paranth, closed_paranth = 0, 0
        result, group_paranth = '', ''

        # To Iiterate in the string
        for bracket in s:
            group_paranth += bracket
            open_paranth += bracket == "("
            closed_paranth += bracket == ")"

            if open_paranth == closed_paranth:
                # The iteration for the outermost parantheses is completed
                # Extract the inner parantheses
                result += group_paranth[1:-1]
                group_paranth = ""
        return result
        