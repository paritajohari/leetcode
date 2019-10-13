class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return (self.replace(address, ".", "[.]"))
        
    def replace(self, string, oldstr, newstr):
        res = ""
        for c in string:
            if c == ".":
                res = res + "[.]"
            else:
                res = res + c
        return res
            