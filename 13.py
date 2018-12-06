class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        finall=0
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
        new=list(s)

        for i in range(len(s)):
            #print(dic[s[i]])
            if i==0:
                print(i)
                finall=dic[s[i]]
                print(finall)
            if i>0 and dic[s[i]]>dic[s[i-1]]:
                finall=dic[s[i]]-finall
            elif i>0 and dic[s[i]]<=dic[s[i-1]]:
                finall+=dic[s[i]]
                print(finall)
        print(finall)
        return finall
a=Solution.romanToInt([],"MCMXCIV")
print(a)