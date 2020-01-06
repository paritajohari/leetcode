'''
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

 

Constraints:

    arr1.length, arr2.length <= 1000
    0 <= arr1[i], arr2[i] <= 1000
    Each arr2[i] is distinct.
    Each arr2[i] is in arr1.


'''

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        '''count_map = {}
        res_arr = []
        for num in arr1:
            if num in count_map.keys():
                count_map[num] = count_map[num] + 1
            else:
                count_map[num] = 1
        
        for num in arr2:
            for count in range(0, count_map[num]):
                res_arr.append(num)
            del count_map[num]
        
        for key in list(sorted(count_map.keys())):
            for count in range(0, count_map[key]):
                res_arr.append(key)
        
        return res_arr
        '''
        
        r = []
        m = {}
        diff = []
        
        for num in arr2:
            if num not in m.keys():
                m[num] = 0
                
        for num in arr1:
            if num in m.keys():
                m[num] = m[num] + 1
            else:
                diff.append(num)
                
        diff.sort()
        
        for num in arr2:
            r.extend([num] * m[num])
        r.extend(diff)
        
        return r
        