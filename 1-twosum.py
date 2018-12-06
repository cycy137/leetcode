class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if target-nums[i] in nums and nums.index(target-nums[i])!=i:
                return [i ,nums.index(target-nums[i])]
        else:
            return None


a=[5,6,4,6]
print(a.__len__())


print(Solution.twoSum([],[3,2,4],6))


