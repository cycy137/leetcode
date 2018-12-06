class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # if len(nums) < 2:
        #     return False
        # mid = []
        # for i in range(len(nums)):
        #
        #     if nums[i] not in mid:
        #         mid.append(nums[i])
        #
        #     else:
        #         print(mid,i)
        #         print(len(mid) - mid.index(nums[i]))
        #         if len(mid) - mid.index(nums[i]) -1 <= k:
        #             return True
        #         else:
        #             return False
        a=dict()
        for ind, val in enumerate(nums):
            print(ind,val)
            a[ind]=val
        print(a)
  # d = dict() # key is num and value is index
  #       for index, n in enumerate(nums):
  #           if n in d.keys() and abs(index - d[n]) <= k:
  #               return True
  #           d[n] = index
  #       return False

a=Solution.containsNearbyDuplicate([],[1,0,1,1],1)
print(a)