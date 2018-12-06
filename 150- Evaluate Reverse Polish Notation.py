class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        tmp = []
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                tmp.append(int(tokens[i]))
            else:
                lastsecond, last = tmp.pop(), tmp.pop()
                if tokens[i] == "+":
                    tmp.append(int(lastsecond + last))
                if tokens[i] == "-":
                    tmp.append(int(lastsecond - last))
                if tokens[i] == "*":
                    tmp.append(int(lastsecond * last))
                if tokens[i] == "/":
                    tmp.append(int(lastsecond / last))
        return tmp[0]
a = Solution.evalRPN([],["2","1","+","3","*"])
print(a)