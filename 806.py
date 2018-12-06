class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype
        """
        a=0
        c=[1,0]
        for i in S :
            b=ord(i)-97
            a+=widths[b]
            if a > 100:
                c[0]+=1
                a=widths[b]
            c[1]=a
        return c

    w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w


