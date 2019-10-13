class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while(True):
            try:
                idx = nums.index(val)
                nums.remove(nums[idx])
            except ValueError as e:
                break
        return len(nums)
        