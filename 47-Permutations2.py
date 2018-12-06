class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        tmp = []
        used = [False ]* len(nums)
        def dfs(nums,mid):
            if len(mid) == len(nums):
                tmp.append(mid[:])
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == True:
                    continue
                used[i]=True
                mid.append(nums[i])
                dfs(nums, mid)
                used[i] = False
                mid.pop()
        dfs(nums, [])
        return tmp
a= Solution.permuteUnique([],[1,1,3])
print(a)