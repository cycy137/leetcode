class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s!=None or s!="":
            for i in s:
                if i in s[s.index(i)+1:]:
                    print(s[s.index(i)+1:])
                    new=s[s.index(i)+1:].split(i)[0]
                    print(new)
                    if new=="":
                        return i+i
                    for j in range(len(new)):

                        if new[j]==new[j][::-1]:
                            print("sdfsd",new[j][::-1])
                            return i+new[j]+i


c=Solution.longestPalindrome([],"baabad")
print(c)
