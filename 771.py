s="aaaaa"
b="a"
c=0
if b in s :
    for b in s:
       c= len(b)
i=0


print("s")
print(c)
class Solution:
    def numJewelsInStones(self, J, S):
    #   if S in J:
    #       return sum(for s in S)
    #   return sum([S.count(j) for j in J])
    #
    # for j in J:
    #     a+=S.count(j))
        a = 0
        for j in J:
            a += S.count(j)
        #return a
        print("a",a)

Solution.numJewelsInStones([],"aaaaaa","a")