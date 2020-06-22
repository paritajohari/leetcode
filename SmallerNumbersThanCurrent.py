'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
 

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
'''

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

    	# Solution:1
        temp_nums = []
        temp_nums.extend(nums)
        temp_nums.sort()
        res_arr = []
        res_map = {temp_nums[0]:0}
        for idx in range(1, len(nums)):            
            if temp_nums[idx] == temp_nums[idx - 1]:
                continue
            if not res_map.get(temp_nums[idx]):
                res_map[temp_nums[idx]] = idx
        for i in nums:
            res_arr.append(res_map[i])
        return res_arr 

        # Solution:2
        # x = sorted(nums)
        # return [x.index(i) for i in nums]