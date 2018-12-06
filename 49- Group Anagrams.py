class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mid = {}
        res = []
        for i in range(len(strs)):
            tmp = list(strs[i])
            tmp.sort()
            if "".join(tmp) not in mid.keys():
                mid["".join(tmp)] = [strs[i]]
            else:
                print("".join(tmp),mid["aet"],mid["".join(tmp)])
                mid["".join(tmp)].append(strs[i])
        print(list(mid.values()))
        return list(mid.values())
a = Solution.groupAnagrams([],["eat", "tea", "tan", "ate", "nat", "bat"])
print(a)