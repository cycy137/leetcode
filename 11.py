class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        final=0
        # for i in range(len(height)):
        #     j = 0
        #     for j in range(len(height)-1):
        #         j+=1
        #         #print(min(i,j),abs(j-i))
        #         print(i,j)
        #         tmp=min(height[i],height[j])*abs(j-i)
        #         #print(tmp)
        #
        #         #print(j)
        #         if tmp>final:
        #             final=tmp
        #
        # return final
            first=0
            end=len(height)-1
            while first<end:
                high = min(height[first], height[end])
                tmp = high * (end-first )
                print(first,end,tmp,high)
                if height[first]>height[end]:
                    end-=1
                else:
                    first+=1

                if tmp>final:
                    final=tmp
            return final
c = Solution.maxArea([],[1,8,6,2,5,4,8,3,7])
print(c)