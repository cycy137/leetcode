class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [];
        def solveWay(nums,tmp):
            if(len(tmp) == len(nums)):
                res.append(tmp[:])
            for i in  range(len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append((nums[i]))
                print("b",nums[i],tmp,i+1)
                solveWay(nums, tmp)
                print("a",nums[i], tmp,i+1)
                tmp.pop()
        solveWay(nums,[]);
        return res
a= Solution.permute([],[1,2,3])
print(a)