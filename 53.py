class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        maximum = running_total = nums[0]

        for n in nums[1:]:
            print(running_total,running_total + n,n)
            running_total = max(running_total + n, n)
            maximum = max(running_total, maximum)

        return maximum

a=Solution.maxSubArray([],[-2,1,-3,4,-1,2,1,-5,4])
print(a)