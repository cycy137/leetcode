class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        long=len(nums)
        print(int(long/2))
        print(long)
        for i in range(len(nums)):
            if nums.count(nums[i])>=int(long/2):
                print(nums[i])
                return nums[i]

a=Solution.majorityElement([],[3,3])
print(a)