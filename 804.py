class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        tran=[]
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for i in range(len(words)):
            temp=[]

            for j in range(len(words[i])):

                temp.append(a[ord(words[i][j])-97])
            #tran.append("".join(temp))
            tran.append(temp)
        print( tran)

Solution.uniqueMorseRepresentations([],["asd","hhj"])

