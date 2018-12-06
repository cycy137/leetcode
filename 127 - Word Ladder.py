class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        lens = 1
        beginList = [beginWord]
        newWordList = set(wordList)
        seen = set(beginList)
        while len(beginList):
            next = []
            for i in range(len(beginList)):
                if beginList[i] == endWord:
                    return lens

            arr = list(beginList[i])
            for j in range(len(arr)):
                for d in range(26):
                    arr[j] = chr(97+d)
                    tmp = "".join(arr)
                    if(tmp not in seen and tmp in newWordList):
                        next.append(tmp)
                        seen.add(tmp)
                arr[j] = beginList[i][j]
            beginList = next
            lens +=1


        return 0
a = Solution.ladderLength([],"hit","cog",["hot","dot","dog","lot","log","cog"])
print(a)