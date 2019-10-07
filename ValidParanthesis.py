class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        value_map = {'(':')','{':'}','[':']'}
        char_len = len(s)
        if char_len%2 != 0:
            return False
        idx = 0
        open_stack = []
        while(idx < char_len):
            if s[idx] in value_map.keys():
                open_stack.append(s[idx])
            elif len(open_stack) != 0 and s[idx] == value_map[open_stack[-1]]:
                open_stack.pop()
            else:
                return False
            idx += 1
        if len(open_stack) != 0:
            return False
        return True
        
        
        