class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=digits.pop()+1
        if a >=10:
            a,b=1,a-10
            digits.append([a,b])
        else:
            digits.append(a)
        return digits