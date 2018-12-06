class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        first,end=0,len(A)-1
        while end>first:
            mid=(first+end)//2
            if (A[mid]>A[mid+1] and A[mid]>A[mid-1]):
                return mid
            elif A[mid]<A[mid-1]:
                end=mid
            else :
                first=mid

Solution.peakIndexInMountainArray([],[0,1,0])