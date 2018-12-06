from collections import Counter
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target = {}
        map = [0 for _ in range(128)]
        print(type(map))
        for c in t:
            target[c] = target.get(c, 0) + 1
        print(target["r"])
        count = len(target)
        start = end = head = 0
        minLen = len(s) + 1
        while end < len(s):

            print(s[end] in target)
            if s[end] in target and  target[s[end]] > 0:
                count -= 1
                target[s[end]] -= 1
            end += 1


            while count == 0:
                if end - start < minLen:
                    minLen = end - start
                    head = start

                if s[start] in target and target[s[start]] == 0:
                    count += 1
                    target[s[start]] +=1
                start +=1
        return s[start:start+minLen]
a = Solution.minWindow([],"ADOBECODEBANC","ABC")
print(a)