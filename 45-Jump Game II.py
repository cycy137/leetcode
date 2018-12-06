class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        curr_reach = 0
        curr_max = 0
        res = 0
        for i in range(len(nums)-1):
            curr_max = max(curr_max, i+nums[i])
            if i == curr_reach:
                res+=1
                curr_reach = curr_max


        return res
a= Solution.jump([],[2,3,1,1,4])
print(a)

# if i + nums[i] > curr_max:
#     next_i = i
#     curr_max = i + nums[i]
# if i == curr_reach:
#
#     if next_i + curr_max <= len(nums) - 1:
#         i = next_i
#         curr_reach = curr_max
#         res += 1