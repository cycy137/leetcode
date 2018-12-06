class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new1=sorted(nums1+nums2)

        if (len(new1))%2==0:

            tmp=(new1[len(new1)//2]+new1[len(new1)//2-1])/2
        else:
            tmp=new1[int(len(new1)/2)]
        return tmp

c=Solution.findMedianSortedArrays([],[1, 3],[2])
print(c)