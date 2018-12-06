class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        finall=0
        nums.sort()
        print(int(len(nums)/2))
        for i in range (0,int(len(nums)),2):
           print("i",i)
           tmp= nums[i],nums[i+1]
           finall+=min(tmp)
        return finall
        print( finall)



a=Solution.arrayPairSum([],[1,3,2,4])
print(a)