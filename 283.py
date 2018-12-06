class Solution:
    def moveZeroes(self, nums):
        # tmp=[]
        # print(len(nums))
        # num_zero=nums.count(0)
        # while 0 in nums:
        #     nums.remove(0)
        # for i in range(num_zero):
        #     tmp.append(0)
        # nums.extend(tmp)
        # return nums
        first=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[first]=nums[first],nums[i]
                first+=1
                print(nums)
        return nums
a=Solution.moveZeroes([],[0,1,0,3,12])
print(a)