class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmp = []
        res = []
        candidates.sort()

        def DFS(candidates, target, curr, tmp, res):
            if target == 0:
                res.append(tmp[::])
                return
            for i in range(curr, len(candidates)):

                if candidates[i] > target: break
                tmp.append(candidates[i])
                DFS(candidates, target - candidates[i], i + 1, tmp, res)
                tmp.pop()

        DFS(candidates, target, 0, tmp, res)
        res = {*res}
        return res
a= Solution.combinationSum2([],[10,1,2,7,6,1,5],8)
print(a)