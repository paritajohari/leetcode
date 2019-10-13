class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        while(idx < len(nums)):
            jdx = idx + 1            
            while(jdx < len(nums)):
                if nums[idx] == nums[jdx]:
                    nums.remove(nums[jdx])                    
                else:
                    break
            idx = idx + 1
            
                    
        
        