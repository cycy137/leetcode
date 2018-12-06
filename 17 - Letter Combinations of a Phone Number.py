class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if not digits:
            return []
        dic = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}


        def dfs(digits, index, tmp):
            if len(digits) == len(tmp):
                res.append("".join(x for x in tmp))
                return
            for i in dic[int(digits[index])]:
                tmp.append(i)
                dfs(digits, index + 1, tmp)
                tmp.pop()

        dfs(digits, 0, [])
        return res

a = Solution.letterCombinations([],"456")
print(a)
