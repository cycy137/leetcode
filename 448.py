class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #tmp=[]
        long=set(list(range(len(nums))))
        long.remove(0)
        short=set(nums)

        tmp=long.difference(short)
        # for i in range(len(long)):
        #     if long[i] not in b:
        #         tmp.append(long[i])
        return tmp





a=Solution.findDisappearedNumbers([],[4,3,2,7,8,2,3,1])
print(a)