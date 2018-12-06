
class Solution:
    def projectionArea(self, grid):
        x=len(grid)
        y=len(grid[0])
        aera=0
        maxX= [0 for i in range(x)]
        maxY=[0 for i in range(y)]
        for xx in range(x):
            for yy in range(y):
                z=grid[xx][yy]
                if z>0:
                    aera+=1
                maxX[xx]=max(maxX[xx],z)
                maxY[yy]=max(maxY[yy],z)
        print(z)
        #return (sum(maxY)+sum(maxX)+aera)

Solution.projectionArea([],[[1,2],[3,7]])