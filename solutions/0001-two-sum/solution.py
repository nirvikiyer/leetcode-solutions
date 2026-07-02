class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for iindex,ival in enumerate(nums):
            for jindex,jval in enumerate(nums):
                if ival + jval == target and iindex != jindex:
                    return [iindex,jindex]
                    break

