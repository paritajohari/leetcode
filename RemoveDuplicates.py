# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         idx = 0
#         while(idx < len(nums)):
#             jdx = idx + 1            
#             while(jdx < len(nums)):
#                 if nums[idx] == nums[jdx]:
#                     nums.remove(nums[jdx])                    
#                 else:
#                     break
#             idx = idx + 1
            
           
# Solution 2:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        N = len(nums)
        for i in range(1, N):
            if nums[start] != nums[i]:
                nums[start + 1] = nums[i]
                start += 1
        return len(nums[:start+1])
                    
        
        
