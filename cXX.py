import copy
class Solution:
    def cXX(self,nums, d):
        curr= []
        res = []
        def DFS(nums, d, n, s, curr, res):

            if  d == n:
                res.append(copy.copy(curr))
                return

            for i in range(s,len(nums)):
                curr.append(nums[i])
                DFS(nums, d + 1, n, i + 1, curr, res)
                curr.pop()
        DFS(nums,0,d,0,curr,res)
        return res

a=Solution.cXX([],[1,2,3],2)
print(a)
