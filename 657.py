class Solution:
    def judgeCircle(self, moves):
       print(moves.count("L"))
       print(moves.count("R"))
       return False if moves.count("L")!=moves.count("R") or moves.count("U")!=moves.count("D") else True



print(Solution.judgeCircle([],"LL"))