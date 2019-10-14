class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for char in str:
            if 65 <= ord(char) <= 90:
                res = res + chr(32 + ord(char))
            else:
                res = res + char
        return res