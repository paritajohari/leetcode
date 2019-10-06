class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        index_map = {'I':0,'V':1,'X':2,'L':3,'C':4,'D':5,'M':6}
        
        res = 0
        idx = 0
        arr_size = len(s)
        
        while idx < arr_size:
            if s[idx] in ['I', 'X', 'C'] and idx < arr_size - 1 and index_map[s[idx + 1]] - index_map[s[idx]] in [1, 2]:
                res += (value_map[s[idx + 1]] - value_map[s[idx]])
                idx += 1
            else:
                res += value_map[s[idx]]
            idx += 1
        return res