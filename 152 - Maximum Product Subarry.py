class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = max(nums)
        minn = 1
        maxx = 1
        for i in range(len(nums)):
            maxx,minn = max(nums[i],nums[i]*minn,nums[i]*maxx),min(nums[i],nums[i]*minn,nums[i]*maxx)

            first = max(maxx,first)
        return first
a=Solution.maxProduct([],[-4,-3,-2])
print(a)