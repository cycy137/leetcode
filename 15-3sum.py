class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        finall = []
        for i in range(len(nums) - 2):
            nexxt,end = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]: continue
            while nexxt < end:
                s = nums[i] + nums[nexxt] + nums[end]
                if s == 0:
                    finall.append([nums[i], nums[nexxt], nums[end]])
                    nexxt += 1
                    end -= 1
                elif s > 0:
                    end -= 1
                else:
                    nexxt += 1
        return finall

a=Solution.threeSum([],[-1, 0, 1, 2, -1, -4])
print(a)