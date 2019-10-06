class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}       
        i = 0
        arr_size = len(s)
        res = 0
        while( i < arr_size ):
            if s[i] == "I" and i < arr_size -1 and s[i+1] == "V":
                res += 4
                i += 1
            elif s[i] == "I" and i < arr_size -1 and s[i+1] == "X":
                res += 9
                i += 1
            elif s[i] == "X" and i < arr_size -1 and s[i+1] == "L":
                res += 40
                i += 1
            elif s[i] == "X" and i < arr_size -1 and s[i+1] == "C":
                res += 90
                i += 1
            elif s[i] == "C" and i < arr_size -1 and s[i+1] == "D":
                res += 400
                i += 1
            elif s[i] == "C" and i < arr_size -1 and s[i+1] == "M":
                res += 900
                i += 1
            else:
                res += value_map[s[i]]
            i += 1
        return res
                
            