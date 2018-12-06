class Solution:
    def hammingDistance(self, x, y):
        x=bin(x)[2:]
        y=bin(y)[2:]
        num=0
        while len(x)>len(y):
            y="0"+y
        while len(y)>len(x):
            x="0"+x
        for i in range(len(x)):
            if x[i]!=y[i]:
                num+=1
        return num

Solution.hammingDistance([],4,6)