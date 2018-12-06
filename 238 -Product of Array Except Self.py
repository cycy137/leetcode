class Solution(object):
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        leftsum = 1
        rightsum = 1

        for i in range(len(nums)):
            result[i] *= leftsum
            result[len(nums) - i - 1] *= rightsum
            leftsum *= nums[i]
            rightsum *= nums[len(nums) - i - 1]

        return result
a = Solution.productExceptSelf([],[1,2,3,4])
print(a)