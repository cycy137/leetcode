import copy
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmp = []
        res = []
        candidates.sort()
        def DFS(candidates,target, curr, tmp, res):
            if target == 0:
                res.append(tmp[:])
                return
            for i in range(curr,len(candidates)):
                if candidates[i] > target:break
                tmp.append(candidates[i])
                DFS(candidates,target-candidates[i], i, tmp, res)
                tmp.pop()
        DFS(candidates,target, 0, tmp, res)
        return res
a = Solution.combinationSum([],[2,3,6,7],7)
print(a)