class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def cond(num):
            s_num = str(num)#1,2,3,4,5
            print("s_sum:",s_num)
            if s_num.count('0') > 0:
                return False   #
            l_nums = map(int, s_num)
            #print(type(l_nums))
            print("l_nums:",list(l_nums))
            print(list(num % i == 0 for i in l_nums))
            #print(all(num % i == 0 for i in l_nums))
            return all(num % i == 0 for i in l_nums)

        return list(filter(cond, [num for num in range(left, right + 1)]))

a=Solution.selfDividingNumbers([],1,22)
print(a)