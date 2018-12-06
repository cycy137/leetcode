class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        if len(nums) < 4:res
        nums.sort()

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:continue
            for j in range(i+1,len(nums) - 2):
                if j > 0 and nums[i] == nums[j - 1]: continue
                first =1
                end = len(nums)-1
                while end > first:
                    summ = nums[i] + nums[j] + nums[first] + nums[end]
                    if summ == target:
                        res.add(tuple([nums[i],nums[j],nums[first],nums[end]]))
                        while first < end and nums[first] == nums[first+1]:first+=1
                        while first < end and nums[end] == nums[end - 1]: end -= 1
                        first+=1
                        end-=1
                    elif summ < target:
                        first+=1
                    elif summ > target:
                        end-=1
        return list(res)

a = Solution.fourSum([],[1, 0, -1, 0, -2, 2],0)
print(a)