class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, a, b):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if a and b:
            if a.val!=b.val:
                return False
        return self.isSameTree(a.left,b.left) and self.isSameTree(a.right,b.right)



a=TreeNode([1,2,3])
b=TreeNode([1,2,3])
c=Solution.isSameTree([],a,b)
print(c)
print(c)