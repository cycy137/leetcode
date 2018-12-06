class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2==0:
            for i in range(len(s)//2):
                s=s.replace("()","")
                s = s.replace("[]", "")
                s = s.replace("{}", "")
                print(i,s)
            if s=="":
                return True
            else:
                return False
        else:
            return False
a=Solution.isValid([],"(([]){})")
print(a)