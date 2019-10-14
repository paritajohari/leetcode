class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res_count = 0
        value_map = {'R':1, 'L':-1}
        value_sum = 0
        for c in s:
            value_sum +=  value_map[c]
            if value_sum == 0:
                res_count += 1
        return res_count