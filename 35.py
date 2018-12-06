class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            print("asdf")
            if target == 0:
                return 0
            i = 0
            while i < len(nums) - 1:

                if nums[i] > target:

                    return i
                    i = lem(nums) + 10
                elif target > nums[-1]:
                    return len(nums)

                i += 1

a=Solution.searchInsert([],[1],2)
print(a)