class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # mid = str.split()
        # a = {}
        # finall = ""
        #
        # for i, j in zip(pattern, mid):
        #     # print(i,j)
        #     if j not in a.values():
        #         a[i] = j
        # print(a)
        # i
        # for i in pattern:
        #     if i in a:
        #         finall += " " + a[i]
        #         print(a[i])
        # print(finall.lstrip(" "))
        # return True if finall.lstrip(" ") == str else False
        str = str.split(" ")
        print(len(set(zip(pattern, str))),len(set(str)),len(set(pattern)))
        print(set(zip(pattern, str)),type(set(zip(pattern, str))))
        return len(set(zip(pattern, str))) == len(set(str)) == len(set(pattern)) and len(pattern) == len(str)
a=Solution.wordPattern([],"abba","dog cat dog cat")
print(a)