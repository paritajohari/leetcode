'''
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:

Input: n = 3
Output: [-1,0,1]

Example 3:

Input: n = 1
Output: [0]

 

Constraints:

    1 <= n <= 1000
'''


class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res_arr = []
        if n % 2 != 0:        
            res_arr.append(0)
            n = n - 1        
        num_pairs = n/2
        for i in range(1, num_pairs+1):
            res_arr.append(i)
            res_arr.append(i * -1)
        return res_arr
        
        '''return range(1 - n, n, 2)'''