class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """   
        if len(strs) == 0:
            return ""
        res = strs[0]        
        for ele in strs[1:]:
            idx = 0
            while(idx < len(res) and idx < len(ele)):
                if(ele[idx] != res[idx]):
                    break
                idx += 1
            res = res[:idx]
            
        return res