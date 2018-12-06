# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """



        def test(root,long):
            if not root:
                return long
            long+=1
            left=test(root.left,long)

            right=test(root.right,long)
            return max(left,right)

        long=1
        answer=0
        return test(root,long)+test(root.right,long)


a=TreeNode([[1,2,3,4,5]])
b=TreeNode([1,2,3])
c=Solution.diameterOfBinaryTree([],a)
print(c)