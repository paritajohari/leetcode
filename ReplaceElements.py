'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

 

Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5
'''

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        last_ele = -1
        max_val = -1
        for idx in range(len(arr)-1, -1,  -1):
            max_val = max(max_val, last_ele)
            last_ele = arr[idx]
            arr[idx] = max_val        
        return arr