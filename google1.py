class Solution :
    def unzip(self,s):
        while "[" in s:
            left = -1
            right = -1
            for i in range(len(s)-1,0,-1):
                if s[i] == "[":
                    left = i
                    break
            for j in range(len(s)):
                if s[j] == "]":
                    right = j
                    break

            if left != -1 and right != -1:
                print(s, s[left - 1:right + 1], s[left + 1:right] * int(s[left - 1]))
                s=s.replace(s[left-1:right+1],s[left+1:right]*int(s[left-1]))

        return s

a= Solution.unzip([],'a3[b2[c1[d]]]e' )
print(a)