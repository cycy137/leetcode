class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        print(len(numbers))
        for i in range(len(numbers)-1):
            mid = 1
            print(mid)
            while numbers[mid]< target and i<len(numbers)-1:
                print(mid,numbers[i], numbers[mid])

                if numbers[i]+numbers[mid]==target:
                    return [i + 1, mid + 1]
                else:
                    mid+=1

a=Solution.twoSum([],[5,25,75],100)
print(a)