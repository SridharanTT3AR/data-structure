class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = []
        count=0
        nums = sorted(nums)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[j]-nums[i]>k):
                    break
                if(nums[j]-nums[i]==k and tuple((min(nums[j],nums[i]),max(nums[j],nums[i]))) not in res):
                    res.append(tuple((min(nums[j],nums[i]),max(nums[j],nums[i]))))
        
        return len(res)
